# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from prontonet.collageteaser.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of prontonet.collageteaser into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if prontonet.collageteaser is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('prontonet.collageteaser'))

    def test_uninstall(self):
        """Test if prontonet.collageteaser is cleanly uninstalled."""
        self.installer.uninstallProducts(['prontonet.collageteaser'])
        self.assertFalse(self.installer.isProductInstalled('prontonet.collageteaser'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IProntonetCollageteaserLayer is registered."""
        from prontonet.collageteaser.interfaces import IProntonetCollageteaserLayer
        from plone.browserlayer import utils
        self.failUnless(IProntonetCollageteaserLayer in utils.registered_layers())
