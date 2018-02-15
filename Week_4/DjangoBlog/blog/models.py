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

    class Meta:
        ordering = ("slug",)

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


class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)