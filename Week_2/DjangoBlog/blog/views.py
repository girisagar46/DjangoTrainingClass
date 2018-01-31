from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Blog


class PostListView(TemplateView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.order_by('-created_date')
        ctx = {"blogs": blogs}
        return render(request, "blog/post.html", context=ctx)


class ContactView(TemplateView):
    template_name = 'blog/contacts.html'


class PostDetailView(TemplateView):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Blog, pk=kwargs.get("pk"))
        ctx = { "post": post }
        return render(request, "blog/post_detail.html", context=ctx)


def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# class PostView(TemplateView):
#     template_name = "blog/post.html"
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(PostView, self).get_context_data(*args, **kwargs)
#         print(context)
#         blogs = Blog.objects.order_by('-created_date')
#         context = {"blogs": blogs}
#
#         return context