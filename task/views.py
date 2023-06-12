from rest_framework.decorators import api_view ,permission_classes 
from django.core.exceptions import PermissionDenied 
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated ,AllowAny 
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework.filters import SearchFilter 
from rest_framework import status 
from django.utils import timezone
from rest_framework.response import Response
from .models import Comment,Task ,DueDate 
from django.db.models import Q
from .serializers import TaskSerializer,CommentSerializer ,DueDateSerializer,CommentsSerializer
from permissions import ISACTIVE ,ISDIRECTOR ,ISSTAFF 
from django.http import HttpRequest 
from django_filters import rest_framework as filters 
from rest_framework.pagination import LimitOffsetPagination

## task view

@api_view(['GET'])
#@permission_classes([IsAuthenticated ,ISSTAFF])
def task_list(request):
    query = request.GET.get('title', '')
    if query:
        queryset =Task.objects.filter(title__icontains=query)
    else:
        queryset = Task.objects.all()
    
     # Initialize the pagination class
    paginator = LimitOffsetPagination()

    # Apply pagination to the queryset
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    serializer = TaskSerializer(paginated_queryset, many=True)

    # Return the paginated response
    return paginator.get_paginated_response(serializer.data)
    

@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
    

@api_view(['PUT'])
#@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    serializer.is_valid(raise_exception =True)
    serializer.save()
    return Response(serializer.data)
    


@api_view(['DELETE'])
def task_delete(request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   

##comment_views 


@api_view(['GET'])
def comment_list(request):
    query = request.GET.get('query', '')
    if query:
        comments = Comment.objects.filter(comment__icontains=query)
    else:
        comments = Comment.objects.all()
    
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
#@permission_classes([IsAuthenticated ,ISDIRECTOR])
def comment_create(request):
    print(request.data)
    serializer = CommentsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)
    


@api_view(['GET'])
def comment_detail(request, pk):
    task = Comment.objects.get(pk=pk)
    serializer = CommentSerializer(task)
    return Response(serializer.data)

@api_view(['PUT'])
def comment_update(request, pk):
    task = Comment.objects.get(pk=pk)
    serializer = CommentSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def comment_delete(request, pk):
    task = Comment.objects.get(pk=pk)
    task.delete()
    return Response(status=204)




#due date views
@api_view(['GET'])
def duedate_list(request):
    query = request.GET.get('query', '')
    
    if query:
        duedates = DueDate.objects.filter(due_date__icontains=query)
    else:
        duedates = DueDate.objects.all()
        
    serializer = DueDateSerializer(duedates, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def duedate_create(request):
    serializer = DueDateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def duedate_detail(request, pk):
    duedate = DueDate.objects.get(pk=pk)
    serializer = DueDateSerializer(duedate)
    return Response(serializer.data)

@api_view(['PUT'])
def duedate_update(request, pk):
    duedate = DueDate.objects.get(pk=pk)
    serializer = DueDateSerializer(instance=duedate, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def duedate_delete(request, pk):
    duedate = DueDate.objects.get(pk=pk)
    duedate.delete()
    return Response(status=204)




@api_view(['GET'])
def task_list_with_comments(request):
    tasks = Task.objects.prefetch_related('comments').all()
    serializer = TaskSerializer(tasks, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def task_list_with_comments_and_due_dates(request):
    tasks = Task.objects.all().prefetch_related('comment_set', 'duedate_set')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comment_wi_task(request):
    comment =Comment.objects.select_related('task').all()
    serializer =CommentSerializer(comment,many =True,context={'request': request})
    return Response(serializer.data)
