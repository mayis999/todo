from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'memo', 'created', 'datecompleted', 'important')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('created',)
    list_editable = ('important',)

admin.site.register(Todo, TodoAdmin)
