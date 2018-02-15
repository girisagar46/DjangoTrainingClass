from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'created_date']
    search_fields = ['title', 'text']
    list_filter = ['created_date', 'author']
    fields = ['title', 'text', 'author']
    list_editable = ['author']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)