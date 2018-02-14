from django import forms

from .models import Blog, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "text",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    text = forms.CharField(max_length=200, widget=forms.Textarea)