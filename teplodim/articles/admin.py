from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Article, File, Image


admin.site.register(Article)
admin.site.register(File)
admin.site.register(Image)
