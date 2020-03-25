from django.db import models


class Scholarship(models.Model):
    UPTO = 'upto'
    EXACT = 'exact'
    AMOUNT_DESCRIPTOR_CHOICES = [
        (UPTO, 'up to'),
        (EXACT, 'exact'),
    ]

    name = models.CharField(max_length=250)
    url = models.URLField(max_length=500)
    amount = models.IntegerField()
    amount_descriptor = models.CharField(
        max_length=5,
        choices=AMOUNT_DESCRIPTOR_CHOICES,
        default=EXACT,
    )
    deadline = models.DateField()

    def __str__(self):
        return self.name
