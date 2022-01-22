from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
#
# gender_choices = [
#     (None, 'Gender'),
#     ('male', 'Male'),
#     ('female', 'Female'),
#     ('other', 'Other')
# ]

class User(AbstractUser):
    # username = None
    name = models.CharField(_('Full Name'), max_length=30, blank=True, null=True)
    username = models.EmailField(_('Username'), unique=True, primary_key=False)
    USERNAME_FIELD = 'username'
    email = models.EmailField(_('email address'), primary_key=False)
    REQUIRED_FIELDS = []

    booking_time = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.email = self.username
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Task(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    roll = models.IntegerField(max_length=10, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    submitted_to = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    bibliography = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)
