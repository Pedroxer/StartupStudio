from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_mask_name = models.CharField(max_length=30)
    user_bio = models.CharField(max_length=300)
    pass
 #   user_name = models.CharField(max_length=30)
  #  user_bio = models.CharField(max_length=300)
    #Additional functionality could be added here
# Create your models here.
