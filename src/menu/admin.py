from django.contrib import admin
from menu.models import Directory

@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'is_root')
    fields = ('name', 'parent', 'is_root')
    ordering = ('-is_root', 'name', )
