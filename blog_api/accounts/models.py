from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Profile(AbstractUser):
    bio = models.TextField(_("Bio"), blank=True)
    avatar = models.ImageField(_("Avatar"), upload_to='avatars/', blank=True)

        # Fix the related_name clashes
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

