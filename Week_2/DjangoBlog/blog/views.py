from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import redirect

from .models import Blog
from .forms import PostForm
from django.contrib.auth.models import User


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


def search(request):
    query = request.GET.get('searchQuery')
    results = []
    count = 0
    if(query):
        results = Blog.objects.filter(
            Q(title__contains=query) |
            Q(text__contains=query)
        )
        count = results.count()
    return render(request, 'blog/results.html', context={'results':results, 'count':count})


@login_required
def post_new(request):
    print(request.__dict__)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = User.objects.get(username=request.username)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})