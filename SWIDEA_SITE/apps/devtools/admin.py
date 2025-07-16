from django.contrib import admin
from .models import Devtool


@admin.register(Devtool)
class DevtoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind')
    search_fields = ('name', 'kind', 'content')