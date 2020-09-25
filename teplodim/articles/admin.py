from django.contrib import admin

from .models import Article, File, Image


class ImageInline(admin.TabularInline):
    model = Image


class FileInline(admin.TabularInline):
    model = File


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
        FileInline
    ]

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
