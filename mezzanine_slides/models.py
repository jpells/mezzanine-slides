try:
    from urllib import unquote
except ImportError:  # assume python3
    from urllib.parse import unquote

from string import punctuation

from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.models import Orderable
from mezzanine.core.fields import FileField


class Slide(Orderable):
    """
    Allows for pretty banner images across the top of pages that will cycle
    through each other with a fade effect.
    """
    page = models.ForeignKey(Page, null=True, blank=True)
    file = FileField(_('File'), max_length=200, upload_to='slides', format='Image')
    description = models.CharField(_('Description'), blank=True, max_length=70)
    caption = models.CharField(_('Caption'), blank=True, max_length=140)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    link = models.CharField(_('Link'), blank=True, max_length=200)

    class Meta:
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
        ordering = ['_order']

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name. If no caption is given when created, create one from
        content_object if exists else use description.
        """
        if not self.id and not self.description:
            name = unquote(self.file.url).split('/')[-1].rsplit('.', 1)[0]
            name = name.replace("'", '')
            name = ''.join([c if c not in punctuation else ' ' for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = ''.join([s.upper() if i == 0 or name[i - 1] == ' ' else s
                            for i, s in enumerate(name)])
            self.description = name
        if not self.id and not self.caption:
            if self.content_object:
                self.caption = self.content_object.title
        super(Slide, self).save(*args, **kwargs)

