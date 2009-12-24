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
from zope.proxy import removeAllProxies
from zope.component import getUtility
from zope.traversing.browser import absoluteURL
from zope.app.component.hooks import getSite
from zope.app.intid.interfaces import IIntIds

from zojax.batching.batch import Batch
from zojax.content.type.interfaces import IItem, IOrder
from zojax.content.attachment.interfaces import IImage, IAttachmentsExtension
from zojax.content.models.container.interfaces import _


class View(object):

    def __init__(self, context, request):
        self.model = context
        super(View, self).__init__(context.__parent__, request)

    def getInfo(self, contentId):
        content = self.container[contentId]

        name = content.__name__
        item = IItem(content, None)

        item = {'id': name,
                'url': '%s/%s/'%(self.url, name),
                'title': getattr(item, 'title', _('No title')) or _('No title'),
                'description':  getattr(item, 'description', ''),
                'image': None}

        if self.showImage:
            image = None
            ids = getUtility(IIntIds)
            url = '%s/@@content.attachment'%absoluteURL(getSite(), self.request)

            extension = IAttachmentsExtension(content, None)
            if extension is None:
                item['image'] = None
            else:
                for attach in extension.values():
                    if IImage.providedBy(attach) and attach:
                        img_url = '%s/%s'%(
                            url, ids.getId(removeAllProxies(attach)))
                        preview = attach.preview.generatePreview(100, 100)

                        image = {'name': attach.__name__,
                                 'title': attach.title,
                                 'image': attach,
                                 'url': img_url,
                                 'purl': '%s/preview/100x100'%img_url}
                        break
                item['image'] = image

        return item

    def update(self):
        model = self.model
        container = self.context

        self.showImage = model.image
        self.url = absoluteURL(container, self.request)

        order = IOrder(container, None)
        if order is not None:
            keys = list(order.keys())
            self.container = order
        else:
            keys = list(container.keys())
            self.container = container

        self.contents = Batch(keys, size=model.pageSize, request=self.request)
