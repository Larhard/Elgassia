from django.db import models


class MenuGeneric(models.Model):
    title = models.CharField(max_length=256)
    dest_name = models.CharField(max_length=256)
    dest_url = models.CharField(max_length=256)

    position = models.IntegerField(default=2147483647)

    def __unicode__(self):
        return '{}'.format(self.title)
