from wsgiref.validate import validator

from django import forms
from django.core import validators

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
    checkBox = forms.BooleanField()
    hidden_val = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['email'].label = ""
        self.fields['text'].label = ""
        self.fields['email'].widget.attrs['placeholder'] = 'email@address.com'
        self.fields['name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['text'].widget.attrs['placeholder'] = 'Write what you want.'