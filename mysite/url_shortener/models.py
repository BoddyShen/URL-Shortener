from django.db import models


class Url(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=15, unique=True)
