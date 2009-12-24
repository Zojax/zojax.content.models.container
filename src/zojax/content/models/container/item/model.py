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
""" content container item view extension

$Id$
"""
from zope import interface, component
from zope.security import checkPermission
from zope.component import getMultiAdapter, queryMultiAdapter
from zope.component.interfaces import ComponentLookupError

from zojax.layout.interfaces import IPagelet
from zojax.content.type.interfaces import IContent, IContentView
from zojax.content.model.interfaces import IModelRenderer
from zojax.content.browser.interfaces import IContainerListing

from interfaces import IContentItem


class ContentItem(object):
    interface.implements(IContentItem)

    def isAvailable(self):
        context = self.context

        for key in context:
            item = context[key]

            if IContent.providedBy(item):
                if checkPermission('zope.View', item):
                    return True

        return False

    def getItem(self):
        return self.context.get(self.item)


@interface.implementer(IModelRenderer)
@component.adapter(IContentItem, interface.Interface)
def getRenderer(view, request):
    item = view.getItem()
    if item is not None:
        return queryMultiAdapter((item, request), IPagelet)
    else:
        return queryMultiAdapter((view.context, request), IContentView)
