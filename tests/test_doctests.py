"""
    CMFPlone doctests.
"""

import os, sys

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

import unittest
from Testing.ZopeTestCase import FunctionalDocFileSuite, FunctionalDocTestSuite
from zope.testing.doctestunit import DocTestSuite
from Products.CMFPlone.tests import PloneTestCase

def test_suite():
    return unittest.TestSuite((
        FunctionalDocTestSuite('Products.CMFPlone.CatalogTool',
                                test_class=PloneTestCase.FunctionalTestCase),
        FunctionalDocTestSuite('Products.CMFPlone.PloneTool',
                                test_class=PloneTestCase.FunctionalTestCase),
        FunctionalDocTestSuite('Products.CMFPlone.TranslationServiceTool',
                                test_class=PloneTestCase.FunctionalTestCase),
        FunctionalDocTestSuite('Products.CMFPlone.CalendarTool',
                                test_class=PloneTestCase.FunctionalTestCase),
        FunctionalDocFileSuite('webdav_index_html_put.txt',
                                package='Products.CMFPlone.tests',
                                test_class=PloneTestCase.FunctionalTestCase),
        DocTestSuite('Products.CMFPlone.utils'),
        ))

if __name__ == '__main__':
    framework()

