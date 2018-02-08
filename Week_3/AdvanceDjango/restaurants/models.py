from datetime import date
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

from .utils import get_age


class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120, null=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=False)
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.location}'


def resuatrant_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
    # instance.age = date.today() - person.dob
    print("Saving......")

def resuatrant_post_save(sender, instance, *args, **kwargs):
    pass


pre_save.connect(resuatrant_pre_save, sender=RestaurantLocation)
post_save.connect(resuatrant_post_save, sender=RestaurantLocation)


class Person(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.CharField(max_length=3, blank=True, null=True)


def person_pre_save(sender, instance, *args, **kwargs):
    instance.age = get_age(instance)


pre_save.connect(person_pre_save, sender=Person)