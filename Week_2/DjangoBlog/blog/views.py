from django.shortcuts import render
from .models import Blog
from django.views import View


def post_list(request):
    blogs = Blog.objects.order_by('-created_date')
    ctx = {
        "blogs": blogs
    }
    return render(request, "blog/post.html", context=ctx)

class PostListView(View):
	def get(self, request, *args, **kwargs):
		blogs = Blog.objects.order_by('-created_date')
		ctx = { "blogs": blogs }
		return render(request, "blog/post.html", context=ctx)
