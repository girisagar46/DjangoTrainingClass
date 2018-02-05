import uuid

from django.db import models
from django.utils.text import slugify


def image_upload_to(instance, filename, *args, **kwargs):
    print(instance)
    title = instance.title
    slug = slugify(title)
    basename, file_extension = filename.split(".")
    new_filename = "{}-{}.{}".format(basename, str(uuid.uuid4()), file_extension)
    return "products/{slug}/{filename}".format(slug = slug, filename=new_filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=image_upload_to)

    def __str__(self):
        return self.title


class Variation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=0, max_digits=20)
    sale_price = models.DecimalField(decimal_places=0, max_digits=20, blank=True, null=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price