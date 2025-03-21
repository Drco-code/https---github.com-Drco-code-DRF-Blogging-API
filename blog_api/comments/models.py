from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

from blog.models import BlogPost
from accounts.models import Profile

# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, verbose_name=_("Post"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    content = models.TextField(_("Content"))
    created_at = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True)


