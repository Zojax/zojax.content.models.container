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
from zope import interface
from zope.security import checkPermission
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zojax.content.type.interfaces import IItem, IContent

from interfaces import IContentItem


class ContainerContents(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        if IContentItem.providedBy(context):
            context = context.context

        terms = []
        for name, content in context.items():
            if IContent.providedBy(content) and \
                   checkPermission('zope.View', content):
                item = IItem(content, None)
                if item is None:
                    title = content.__name__
                else:
                    title = u'%s (%s)'%(item.title, content.__name__)
                terms.append((title, SimpleTerm(name, name, title)))

        terms.sort()
        return SimpleVocabulary([term for t, term in terms])
