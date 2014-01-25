from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class SiteUserManager(BaseUserManager):
    def create_user(self, email, name, password, **kwargs):
        user = self.model(
            email=email,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class SiteUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [name]

    objects = SiteUserManager()

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_superuser
