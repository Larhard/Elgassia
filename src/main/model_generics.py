from django.db import models


class MenuGeneric(models.Model):
    title = models.CharField(max_length=256, default='')
    dest_name = models.CharField(max_length=256, default='')
    dest_url = models.CharField(max_length=256, default='')
    dest_page = models.CharField(max_length=256, default='')

    position = models.IntegerField(default=2147483647)

    def __unicode__(self):
        return '{}'.format(self.title)


class PageGeneric(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()

    # TODO permissions

    def __unicode__(self):
        return '{}'.format(self.title)
