from django.contrib import admin
from django.contrib.auth.models import User
from .models import Task 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'get_tags']
    search_fields = ['title', 'tags']
    date_hierarchy = 'due_date'

    def get_tags(self, obj):
    	return obj.tags.names()