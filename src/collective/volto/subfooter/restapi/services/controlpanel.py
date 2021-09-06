# -*- coding: utf-8 -*-
from collective.volto.subfooter.interfaces import (
    ICollectiveVoltoSubfooterLayer,
    ISubfooter,
)
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(Interface, ICollectiveVoltoSubfooterLayer)
@implementer(ISubfooter)
class SubfooterControlpanel(RegistryConfigletPanel):
    schema = ISubfooter
    configlet_id = "Subfooter"
    configlet_category_id = "Products"
    schema_prefix = None
