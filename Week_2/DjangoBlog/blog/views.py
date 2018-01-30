from django.shortcuts import render
from .models import Blog


def post_list(request):
    blogs = Blog.objects.order_by('-created_date')
    ctx = {
        "blogs": blogs
    }
    return render(request, "blog/post.html", context=ctx)


