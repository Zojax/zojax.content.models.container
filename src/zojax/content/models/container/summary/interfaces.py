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
from zope import interface, schema
from zojax.richtext.field import RichText
from zojax.content.models.container.interfaces import _


class IFolderSummaryModel(interface.Interface):
    """ folder summary model """

    image = schema.Bool(
        title = _(u'Image'),
        description = _(u'Use image previews for item.'),
        default = False,
        required = False)

    pageSize = schema.Int(
        title = _(u'Page size'),
        description = _(u'Number of items per page.'),
        default = 20,
        required = False)

    text = RichText(
        title = _(u'Text'),
        description = _(u'Folder preview text.'),
        required = False)
