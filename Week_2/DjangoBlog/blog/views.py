from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.shortcuts import redirect

from blog.serializers import BlogSerializer
from .models import Blog
from .forms import PostForm, CommentForm, ContactForm
from DjangoBlog.settings import DEFAULT_FROM_EMAIL, BLOG_NAME


class PostListView(TemplateView):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.order_by('-created_date')
        ctx = {"blogs": blogs}
        return render(request, "blog/post.html", context=ctx)


class ContactView(TemplateView):
    pass
    # template_name = 'blog/contacts.html'


def contact_us(request):
    contact_form = ContactForm()
    if request.method == "POST":
        if contact_form.is_valid():
            print("Form Valid")
            name = request.POST.get('name', '')
            user_email = request.POST.get('email', '')
            text = request.POST.get('text', '')
            context = {
                'name': name,
                'email': user_email,
                'text': text,
            }
            template = get_template('contact_template.txt')
            content = template.render(context=context)
            email = EmailMessage(
                "New comment is added in your blog.",
                content,
                BLOG_NAME + '',
                [DEFAULT_FROM_EMAIL],
                headers={'Reply-To': user_email}
            )
            email.send()
            return redirect('contact')
        else:
            print("Form InValid")
            return redirect('contact')
    return render(request, 'blog/contacts.html', {"contact_form": contact_form})


class PostDetailView(TemplateView):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Blog, pk=kwargs.get("pk"))
        comments = post.comments.filter(active=True)
        comment_form = CommentForm()
        ctx = { "post": post, "comments":comments , "comment_form":comment_form}
        return render(request, "blog/post_detail.html", context=ctx)

    @login_required
    def post(self, request, *args, **kwargs):
        print("post called")
        print(request.__dict__)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            post = get_object_or_404(Blog, pk=kwargs.get("pk"))
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', pk=post.pk)

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

@csrf_exempt
def blog_list(request, **kwargs):
    """
    List all code snippets, or create a new snippet.
    """
    qs = request.META['QUERY_STRING']
    q, l = qs.split("=")
    if request.method == 'GET':
        if(qs):
            snippets = Blog.objects.all()[:int(l)]
        else:
            snippets = Blog.objects.all()
        serializer = BlogSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

def blog_detail(request, **kwargs):
    pass
    # pk = kwargs.get('pk')
    # snippets = Blog.objects.get(pk=pk)
    # serializer = BlogSerializer(snippets, many=True)
    # print(serializer.data)
    # return JsonResponse(serializer.data, safe=False)