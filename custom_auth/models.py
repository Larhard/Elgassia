from django.db import models
import django.contrib.auth.models as django


class CustomUserManager(django.UserManager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD+'__iexact': username})


class CustomUser(django.AbstractUser):
    objects = CustomUserManager()
