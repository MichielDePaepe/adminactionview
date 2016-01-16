from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ModelExample(models.Model):
    value = models.IntegerField()

    def __unicode__(self):
        return "The value is: %i" % self.value
