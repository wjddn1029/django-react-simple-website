from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
