# -*- coding: utf-8 -*-
from collective.volto.subfooter.interfaces import ISubfooter
from collective.volto.subfooter.restapi.serializer.subfooter import serialize_data
from plone import api
from plone.restapi.services import Service
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


@implementer(IPublishTraverse)
class SubfooterGet(Service):
    def __init__(self, context, request):
        super(SubfooterGet, self).__init__(context, request)

    def reply(self):
        try:
            record = api.portal.get_registry_record(
                "subfooter_configuration", interface=ISubfooter, default="",
            )
        except KeyError:
            return []
        if not record:
            return []
        return serialize_data(json_data=record)
