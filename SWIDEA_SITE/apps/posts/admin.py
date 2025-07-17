from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'interest', 'devtool', 'created_at')
    list_filter = ('devtool',)
    search_fields = ('title', 'content')