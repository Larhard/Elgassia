import django.contrib.auth.models as django
from django.db import IntegrityError


class CustomUserManager(django.UserManager):
    def _create_user(self, username, *args, **kwargs):
        try:
            if username and self.get_by_natural_key(username):
                raise IntegrityError(self.model.USERNAME_FIELD + " not unique")
        except self.model.DoesNotExist:
            pass

        super(CustomUserManager, self)._create_user(username, *args, **kwargs)

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD+'__iexact': username})


class CustomUser(django.AbstractUser):
    objects = CustomUserManager()
