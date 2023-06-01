from django.contrib import admin
from .models import Task,Comment,DueDate


admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(DueDate)