# -*- coding: utf-8 -*-
from collective.volto.subfooter import _
from plone.restapi.controlpanels.interfaces import IControlpanel
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.schema import SourceText
import json


class ISubfooter(IControlpanel):
    subfooter_configuration = SourceText(
        title=_("subfooter_configuration_label", default="Subfooter configuration",),
        description="",
        required=True,
        default=json.dumps([{"rootPath": "/", "items": []}]),
    )


class ICollectiveVoltoSubfooterLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
