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
""" content container listing extension

$Id$
"""
from zope import interface
from zope.component import queryMultiAdapter
from zope.security.management import checkPermission
from zojax.content.type.interfaces import IContentView
from zojax.content.model.interfaces import IModelRenderer
from zojax.content.browser.interfaces import IContainerListing


class ContentListing(object):
    interface.implements(IModelRenderer, IContentView)

    def update(self):
        self.view = queryMultiAdapter(
            (self.context, self.request), IContainerListing)

    def render(self):
        self.view.update()
        return self.view.render()

    def isAvailable(self):
        return self.view and checkPermission('zope.View', self.context)
