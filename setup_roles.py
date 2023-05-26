from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from task.models import Task

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo_app.settings')
django.setup()
def setup_roles():
    # Create roles (groups)
    admin_group, _ = Group.objects.get_or_create(name='admin_control')
    director_group, _ = Group.objects.get_or_create(name='director')
    student_group, _ = Group.objects.get_or_create(name='student')

    # Create users
    admin_user, _ = User.objects.get_or_create(username='admin_first')
    director_user, _ = User.objects.get_or_create(username='director')
    student_user, _ = User.objects.get_or_create(username='student')

    # Assign users to roles
    admin_user.groups.set([admin_group])
    director_user.groups.set([director_group])
    student_user.groups.set([student_group])

    # Define model-level permissions
    content_type = ContentType.objects.get_for_model(Task)
    can_add_task_permission, _ = Permission.objects.get_or_create(codename='can_add_task', name='Can add task', content_type=content_type)
    can_delete_task_permission, _ = Permission.objects.get_or_create(codename='can_delete_task', name='Can delete task', content_type=content_type)

    # Assign permissions to roles
    admin_group.permissions.set([can_add_task_permission, can_delete_task_permission])
    director_group.permissions.set([can_add_task_permission])
    student_group.permissions.set([])  # No permissions for students

if __name__ == '__main__':
    setup_roles()
