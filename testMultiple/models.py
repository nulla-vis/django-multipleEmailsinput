from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class User(models.Model):
    user = models.CharField(max_length=255, blank=True)


class Email(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email_list = models.EmailField(max_length=70)
