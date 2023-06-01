from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group, Permission

'''💡The roles are enough for the present models but when we scale the project we have to manually code '''
'''💡by default every loginned user is not staff(employee)...admin will make them employee'''


class UserAccountManager(BaseUserManager):
    
    def create_user(self, username,email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    objects = UserAccountManager()

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) 
    is_superuser=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_director = models.BooleanField(default=False)
    is_vice_director=models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='user_accounts', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_accounts', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_user_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email
