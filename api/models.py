from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    about = models.TextField()
    phone = models.CharField(max_length=10)
    country = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"