from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=75)
    text = models.TextField(max_length=10000, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
