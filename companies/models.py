from django.db import models
from datetime import datetime
from founders.models import Founder

class Company(models.Model):
    founder = models.ForeignKey(Founder, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    profession = models.CharField(max_length=15)
    website = models.CharField(max_length=30)
    description = models.CharField(blank=True)
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_listed = models.BooleanField(default=True)
    is_boosted = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    def __str__(self):
        return self.title