from django.db import models

import model_generics


class MainMenu(model_generics.MenuGeneric):
    pass


class StandardPage(model_generics.PageGeneric):
    pass


class Config(models.Model):
    key = models.CharField(max_length=256, unique=True)
    value = models.CharField(max_length=256)

    def __unicode__(self):
        return "{}".format(self.key)
