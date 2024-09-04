from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    heartRate = models.IntegerField()
    # incline = models.IntegerField()
    experience = models.CharField(max_length=20)
    goalDistance = models.IntegerField()
    distanceCovered = models.IntegerField()
    result = models.TextField()
    requestDateTime = models.DateTimeField(default=timezone.now)

