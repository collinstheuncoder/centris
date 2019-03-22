from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phone_field import PhoneField

# Create your models here.
class CustomUserManager(UserManager):
		pass

class CustomUser(AbstractUser):
		objects = CustomUserManager()
		phone = PhoneField(blank=True,)
