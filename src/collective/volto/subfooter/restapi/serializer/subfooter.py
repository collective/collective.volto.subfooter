# -*- coding: utf-8 -*-
from AccessControl.unauthorized import Unauthorized
from collective.volto.subfooter.interfaces import ISubfooter
from plone import api
from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.interfaces import ISerializeToJsonSummary
from plone.restapi.serializer.controlpanels import ControlpanelSerializeToJson
from plone.restapi.serializer.converters import json_compatible
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.globalrequest import getRequest
from zope.interface import implementer

import json

KEYS_WITH_URL = ["linkUrl", "navigationRoot", "showMoreLink"]


def serialize_data(json_data):
    if not json_data:
        return ""
    data = json.loads(json_data)
    for root in data:
        for tab in root.get("items", []):
            for key in KEYS_WITH_URL:
                value = tab.get(key, [])
                if value:
                    serialized = []
                    for uid in value:
                        try:
                            item = api.content.get(UID=uid)
                        except Unauthorized:
                            continue
                        if not item:
                            continue
                        summary = getMultiAdapter(
                            (item, getRequest()), ISerializeToJsonSummary
                        )()
                        if summary:
                            # serializer doesn't return uid
                            summary["UID"] = uid
                            serialized.append(summary)
                    tab[key] = serialized
    return json_compatible(data)


@implementer(ISerializeToJson)
@adapter(ISubfooter)
class SubfooterControlpanelSerializeToJson(ControlpanelSerializeToJson):
    def __call__(self):
        json_data = super(SubfooterControlpanelSerializeToJson, self).__call__()
        conf = json_data["data"].get("subfooter_configuration", "")
        if conf:
            json_data["data"]["subfooter_configuration"] = json.dumps(
                serialize_data(json_data=conf)
            )
        return json_data
