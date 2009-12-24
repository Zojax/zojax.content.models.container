##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
import os, unittest, doctest
from zope import interface
from zope.app.intid import IntIds
from zope.app.intid.interfaces import IIntIds
from zope.app.testing.functional import getRootFolder

from zojax.content.model.tests import content
from zojax.filefield.testing import ZCMLLayer, FunctionalDocFileSuite
from zojax.content.attachment.interfaces import IAttachmentsAware
from zojax.content.models.container.interfaces import IContainerModelsAware

zojaxContainerModelsLayer = ZCMLLayer(
    os.path.join(os.path.split(__file__)[0], 'ftesting.zcml'),
    __name__, 'zojaxContainerModelsLayer', allow_teardown=True)


def setUp(test):
    root = getRootFolder()

    root['ids'] = IntIds()
    root.getSiteManager().registerUtility(root['ids'], IIntIds)

    if 'container' not in root:
        root['container'] = content.MyContentContainer(u'My Container')
        interface.alsoProvides(
            root['container'],
            IAttachmentsAware, IContainerModelsAware)
        root['container']['content1'] = content.MyContent(
            u'My Content 1', description=u'My Content 1 description',)
        interface.alsoProvides(root['container']['content1'], IAttachmentsAware)
        root['container']['content2'] = content.MyContent(
            u'My Content 2', description=u'My Content 2 description',)
        interface.alsoProvides(root['container']['content2'], IAttachmentsAware)
        root['container']['content3'] = content.MyContent(
            u'My Content 3', description=u'My Content 3 description',)
        interface.alsoProvides(root['container']['content3'], IAttachmentsAware)
        root['container']['content4'] = content.MyContent(
            u'My Content 4', description=u'My Content 4 description',)
        interface.alsoProvides(root['container']['content4'], IAttachmentsAware)
        root['container']['content5'] = content.MyContent(
            u'My Content 5', description=u'My Content 5 description',)
        interface.alsoProvides(root['container']['content5'], IAttachmentsAware)
        root['container']['content6'] = content.MyContent(
            u'My Content 6', description=u'My Content 6 description',)
        interface.alsoProvides(root['container']['content6'], IAttachmentsAware)

    if 'container2' not in root:
        root['container2'] = content.MyContentContainer(u'My Container 2')
        interface.alsoProvides(
            root['container2'],
            IAttachmentsAware, IContainerModelsAware)

def test_suite():
    item = FunctionalDocFileSuite("item.txt", setUp=setUp)
    item.layer = zojaxContainerModelsLayer

    listing = FunctionalDocFileSuite("listing.txt", setUp=setUp)
    listing.layer = zojaxContainerModelsLayer

    summary = FunctionalDocFileSuite("summary.txt", setUp=setUp)
    summary.layer = zojaxContainerModelsLayer

    return unittest.TestSuite((item, listing, summary))
