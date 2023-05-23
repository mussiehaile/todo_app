from django.urls import path
from .views import user_list,user_detail

app_name = 'accounts'

urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('users/<int:user_id>/', user_detail, name='user-delete')
]
