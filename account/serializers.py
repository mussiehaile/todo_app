from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 
from rest_framework import serializers
from django.contrib.auth import get_user_model
from account.models import UserAccount




# class MyUserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = MyUser
#         fields = ('username','email', 'password', 'first_name', 'last_name')


# class MyUserSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#         model = MyUser
#         fields = ('email', 'first_name', 'last_name')

User = get_user_model()
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = UserAccount
        fields = ['id', 'email', 'username', 'password','is_active','is_superuser','is_staff','is_director','is_vice_director']



class UserAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id','username','email']





























































































# from rest_framework import serializers
# from .models import UserAccount

# class UserAccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAccount
#         fields = ['id', 'email', 'username', 'is_active', 'is_superuser', 'is_staff', 'is_director', 'is_vice_director']
#         read_only_fields = ['id']














# from djoser.serializers import UserCreateSerializer, UserSerializer
# from account.models import MyUser  # Replace 'accounts' with your app name

