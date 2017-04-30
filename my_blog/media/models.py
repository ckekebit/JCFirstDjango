from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Media(models.Model):
    mediaName = models.CharField(max_length = 30)
    mediaPath = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.mediaName

admin.site.register(Media)
