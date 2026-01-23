# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.volto.subfooter.testing import VOLTO_SUBFOOTER_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.volto.subfooter is properly installed."""

    layer = VOLTO_SUBFOOTER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def _is_product_installed(self, product_id):
        if hasattr(self.installer, "is_product_installed"):
            return self.installer.is_product_installed(product_id)
        return self.installer.isProductInstalled(product_id)

    def test_product_installed(self):
        """Test if collective.volto.subfooter is installed."""
        self.assertTrue(
            self._is_product_installed("collective.volto.subfooter")
        )

    def test_browserlayer(self):
        """Test that ICollectiveVoltoSubfooterLayer is registered."""
        from collective.volto.subfooter.interfaces import ICollectiveVoltoSubfooterLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveVoltoSubfooterLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = VOLTO_SUBFOOTER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        if hasattr(self.installer, "uninstall_product"):
            self.installer.uninstall_product("collective.volto.subfooter")
        else:
            self.installer.uninstallProducts(["collective.volto.subfooter"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def _is_product_installed(self, product_id):
        if hasattr(self.installer, "is_product_installed"):
            return self.installer.is_product_installed(product_id)
        return self.installer.isProductInstalled(product_id)

    def test_product_uninstalled(self):
        """Test if collective.volto.subfooter is cleanly uninstalled."""
        self.assertFalse(
            self._is_product_installed("collective.volto.subfooter")
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveVoltoSubfooterLayer is removed."""
        from collective.volto.subfooter.interfaces import ICollectiveVoltoSubfooterLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveVoltoSubfooterLayer, utils.registered_layers())
