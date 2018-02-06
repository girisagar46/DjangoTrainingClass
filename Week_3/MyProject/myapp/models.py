from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120, blank=False)
    price = models.FloatField()

    def __str__(self):
        return self.title