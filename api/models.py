from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    streem_platform = models.CharField(max_length=255, blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)
    review = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"Movie name:{self.name}"
