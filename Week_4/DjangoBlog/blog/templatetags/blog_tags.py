from datetime import datetime

from django import template
from django.db.models import Q

import DjangoBlog.settings as settings
from blog.models import Blog

register = template.Library()


@register.simple_tag
def blog_name():
    return settings.BLOG_NAME


@register.simple_tag
def blog_count():
    return Blog.objects.all().count()


@register.inclusion_tag('blog/latest.html')
def latest(count=None):
    latest_blog = []
    if count is not None:
        latest_blog = Blog.objects.all()[:count]
    else:
        latest_blog =  Blog.objects.all()
    return {"latest_blog":latest_blog}


@register.inclusion_tag('blog/snippets/footer.html')
def footer():
    return {"year":datetime.today().year}


@register.assignment_tag
def similar(query, qpk):
    results = []
    if(query):
        results = Blog.objects.filter(
            Q(title__contains=query) |
            Q(text__contains=query)
        ).exclude(pk=qpk)
    return results


@register.filter
def capitalizeTitle(title):
    return title.upper()