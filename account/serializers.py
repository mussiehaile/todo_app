# serializers.py

from djoser.serializers import UserCreateSerializer, UserSerializer
from account.models import MyUser  # Replace 'accounts' with your app name


class MyUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = MyUser
        fields = ('username','email', 'password', 'first_name', 'last_name')


class MyUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = MyUser
        fields = ('email', 'first_name', 'last_name')
