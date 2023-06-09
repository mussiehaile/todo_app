#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserAccount 
from.serializers import UserAccountSerializers


@api_view(['GET'])
def user_list(request):
    users = UserAccount.objects.all()
    serializer = UserAccountSerializers(users, many=True)
    return Response(serializer.data)

# @api_view(['GET', 'DELETE'])
# def user_detail(request, user_id):
#     try:
#         user = MyUser.objects.get(id=user_id)
#     except MyUser.DoesNotExist:
#         return Response({'message': 'User not found'}, status=404)
    
#     if request.method == 'GET':
#         serializer = MyUserSerializer(user)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response({'message': 'User deleted successfully'})