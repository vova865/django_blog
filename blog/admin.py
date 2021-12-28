from django.contrib import admin

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create',)
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'city')
    list_display_links = ('first_name', 'city')
    search_fields = ('first_name', 'last_name', 'city')
    prepopulated_fields = {"slug": ("first_name",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Writer, WriterAdmin)
