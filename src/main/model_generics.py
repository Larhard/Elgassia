from django.db import models


class MenuGeneric(models.Model):
    title = models.CharField(max_length=256)
    dest_name = models.CharField(max_length=256)
    dest_url = models.CharField(max_length=256)

    # TODO positioning system

    def __unicode__(self):
        return '{}'.format(self.title)
