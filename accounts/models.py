from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import FiliUserManager
# Create your models here.

class FiliUser(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=10, choices=(("Mr", "Mr"), ("Ms", "Ms"), ("Mrs", "Mrs"),  ("Others", "Others")))
    is_verified = models.BooleanField(default=False)
    mobile = models.CharField(max_length=14, null=False)
    about_me = models.CharField(max_length=500)
# location
# who am i ( user type )
    languages = models.CharField(max_length=50)

    objects = FiliUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []