# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.restapi.testing import PloneRestApiDXLayer
from plone.testing import z2

import collective.volto.subfooter
import plone.restapi


class VoltoSubfooterLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.subfooter)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.volto.subfooter:default")


VOLTO_SUBFOOTER_FIXTURE = VoltoSubfooterLayer()


VOLTO_SUBFOOTER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VOLTO_SUBFOOTER_FIXTURE,), name="VoltoSubfooterLayer:IntegrationTesting",
)


VOLTO_SUBFOOTER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VOLTO_SUBFOOTER_FIXTURE,), name="VoltoSubfooterLayer:FunctionalTesting",
)


class VoltoSubfooterRestApiLayer(PloneRestApiDXLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        super(VoltoSubfooterRestApiLayer, self).setUpZope(app, configurationContext)

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.subfooter)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.volto.subfooter:default")


VOLTO_SUBFOOTER_API_FIXTURE = VoltoSubfooterRestApiLayer()
VOLTO_SUBFOOTER_API_INTEGRATION_TESTING = IntegrationTesting(
    bases=(VOLTO_SUBFOOTER_API_FIXTURE,), name="VoltoSubfooterRestApiLayer:Integration",
)

VOLTO_SUBFOOTER_API_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(VOLTO_SUBFOOTER_API_FIXTURE, z2.ZSERVER_FIXTURE),
    name="VoltoSubfooterRestApiLayer:Functional",
)
