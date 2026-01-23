# -*- coding: utf-8 -*-
from collective.volto.subfooter import _
from collective.volto.subfooter.interfaces import ISubfooter
from plone.app.registry.browser import controlpanel


class SubfooterForm(controlpanel.RegistryEditForm):

    schema = ISubfooter
    label = _("subfooter_settings_label", default="Subfooter Settings")
    description = ""


class Subfooter(controlpanel.ControlPanelFormWrapper):
    form = SubfooterForm
