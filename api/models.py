from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    streem_platform = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Movie name:{self.name}"
