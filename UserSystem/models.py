from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=30)
    role_description = models.CharField(max_length=800)

    def __str__(self):
        return self.role_name

class CustomUser(AbstractUser):
    user_mask_name = models.CharField(max_length=30)
    user_bio = models.CharField(max_length=300)
    roles = models.ManyToManyField(Role) #One user could have many roles
    pass
 #   user_name = models.CharField(max_length=30)
  #  user_bio = models.CharField(max_length=300)
    #Additional functionality could be added here
# Create your models here.
