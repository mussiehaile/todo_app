from django.urls import path
from .views import task_list, task_create, task_detail, \
task_update, task_delete,task_list_with_comments,comment_list, \
comment_create ,comment_delete,comment_detail,comment_update ,duedate_create ,duedate_delete ,duedate_detail,duedate_list,\
duedate_update,task_list_with_comments_and_due_dates ,comment_wi_task 
    

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks/create/', task_create, name='task-create'),
    path('tasks/<int:pk>/', task_detail, name='task-detail'),
    path('tasks/<int:pk>/update/', task_update, name='task-update'),
    path('tasks/<int:pk>/delete/', task_delete, name='task-delete'),
    
    path('tasks/filter', task_list, name='task-list'),

    path('t&c/', task_list_with_comments, name='task-list-with-comments'),
    path('tasks/due', task_list_with_comments_and_due_dates, name='task-list'),
    path('com_with_task/', comment_wi_task, name='comment-wi-task'),
    
    path('comments/', comment_list, name='comment-list'),
    path('comments/create', comment_create, name='comment-create'),
    path('comments/<int:pk>/', comment_detail, name='comments-detail'),
    path('comments/<int:pk>/update/', comment_update, name='comments-update'),
    path('comments/<int:pk>/delete/', comment_delete, name='comments-delete'),
    
    path('duedates/', duedate_list, name='duedate-list'),
    path('duedates/create/', duedate_create, name='duedate-create'),
    path('duedates/<int:pk>/', duedate_detail, name='duedate-detail'),
    path('duedates/<int:pk>/update/', duedate_update, name='duedate-update'),
    path('duedates/<int:pk>/delete/', duedate_delete, name='duedate-delete'),
]
