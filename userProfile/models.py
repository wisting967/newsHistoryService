from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
  pass

  class Meta:
    db_table = 't_userprofile'