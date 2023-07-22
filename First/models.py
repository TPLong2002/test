from django.db import models

class Value(models.Model):
    Value = models.CharField(max_length=10)
    Time = models.TimeField(auto_now=True)

