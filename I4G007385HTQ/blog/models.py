from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_Date = models.DateTimeField()
    Published_Date = models.DateTimeField()