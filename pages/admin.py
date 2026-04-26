from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'subtitle', 'content')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
