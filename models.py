from django.db import models
from .managers import EmailUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class EmailUser(AbstractUser):
    email = models.EmailField(
        'email',
        unique=True,
        help_text=_('Required.'),
        error_messages={
            'unique': _('A user with that email already exists.'),
        }
    )

    username = None
    username_validator = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = EmailUserManager()

    class Meta:
        verbose_name = 'user'
