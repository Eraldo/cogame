from django.contrib import admin
from tasks.models import Task
from lib.admin import InlineMixin

__author__ = 'eraldo'


class TaskInline(InlineMixin, admin.TabularInline):
    model = Task
    fields = ['name', 'status', 'date', 'deadline', 'tags', 'owner', 'change_link']
    extra = 0
    readonly_fields = ['change_link']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'deadline', 'date', 'project', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['status', 'tags', 'owner']
    filter_horizontal = ['tags']
    readonly_fields = ['creation_date', 'modification_date', 'history']

    fieldsets = [
        (None, {'fields': ['owner', 'project']}),
        (None, {'fields': ['name', 'description']}),
        (None, {'fields': ['status', 'deadline', 'date', 'tags']}),
        ('history', {'fields': ['creation_date', 'modification_date', 'history'], 'classes': ['collapse']}),
    ]


admin.site.register(Task, TaskAdmin)