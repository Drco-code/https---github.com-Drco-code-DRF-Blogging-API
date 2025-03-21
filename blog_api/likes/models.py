from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models import BlogPost
from django.contrib.auth.models import User

# Create your models here.

class LikeDislike(models.Model):

    class LikeDislike(models.TextChoices):
        LIKE = 'L', _("Like")
        DISLIKE = 'D', _('Dislike')

    post = models.ForeignKey(BlogPost, verbose_name=_("Post"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    type = models.CharField(_("Rating"), max_length=1, choices=LikeDislike)

    class Meta:
        unique_together = ('post', 'user')