# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from collective.volto.subfooter.interfaces import ISubfooter
from collective.volto.subfooter import _


class SubfooterForm(controlpanel.RegistryEditForm):

    schema = ISubfooter
    label = _("subfooter_settings_label", default=u"Subfooter Settings")
    description = u""


class Subfooter(controlpanel.ControlPanelFormWrapper):
    form = SubfooterForm
