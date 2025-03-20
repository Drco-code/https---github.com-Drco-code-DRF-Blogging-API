from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Profile

# Create your models here.

class BlogPost(models.Model):

    class StatusChoices(models.TextChoices):
        PUBLISHED = 'P', _("Published")
        DRAFT = 'D', _("Draft")
        ARCHIVED = 'A', _("Archived")


    title = models.CharField(_("Title"), max_length=255)
    content = models.TextField(_("Content"))
    author = models.ForeignKey(Profile, verbose_name=_("Author"), on_delete=models.CASCADE)
    status = models.CharField(_("Status"), max_length=1, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
    created_at = models.DateTimeField(_("Creation Date"),  auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)
    models.ImageField(_("Blog Image"), upload_to='blog_images/', blank=True)

    def __str__(self):
        return self.title