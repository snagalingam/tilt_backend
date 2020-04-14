from django.conf import settings
from django.db import models


class Scholarship(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    deadline = models.DateField()
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.name
