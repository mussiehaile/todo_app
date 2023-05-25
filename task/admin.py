from django.contrib import admin
from django.http.request import HttpRequest
from .models import Task,Comment ,DueDate




class MyModelAdmin(admin.ModelAdmin):
    pass



class ReadOnlyAdminMixin:
    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request ,obj = None):
        return False
    def has_delete_permission(self, request ,obj =None):
        return False
    def has_view_permission(self, request , obj = None):
        return True
    

@admin.register(Task)
class TaskAdmin( ReadOnlyAdminMixin,admin.ModelAdmin):
    list_display =('title',)
    