from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone

from .utils import unique_slug_generator


class Blog(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=120)
    text = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @property
    def field(self):
        return str(self.author.username+self.title)


def blog_pre_save(sender, instance, *args, **kwargs):
    pass


def blog_post_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()


pre_save.connect(receiver=blog_pre_save, sender=Blog)
post_save.connect(receiver=blog_post_save, sender=Blog)


# class Tags(models.Model):
#     blog = models.ForeignKey('Blog')
#     tagname = models.CharField(max_length=10)
#     slug = models.SlugField(blank=True, null=True)
#
#     def __str__(self):
#         return self.tagname
#
#     @property
#     def field(self):
#         return str(self.tagname+self.blog.title)
#
#
# def tag_pre_save(sender, instance, *args, **kwargs):
#     pass
#
#
# def tag_post_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()
#
#
# pre_save.connect(receiver=tag_pre_save, sender=Tags)
# post_save.connect(receiver=tag_post_save, sender=Tags)