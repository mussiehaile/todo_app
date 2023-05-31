from rest_framework.decorators import api_view ,permission_classes 
from django.core.exceptions import PermissionDenied 
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated ,AllowAny 
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .models import Comment,Task ,DueDate
from .serializers import TaskSerializer,CommentSerializer ,DueDateSerializer
from permissions import ISACTIVE ,ISDIRECTOR ,ISSTAFF

## task view

@api_view(['GET'])
@permission_classes([IsAuthenticated ,ISSTAFF])
def task_list(request):
        print('oooooooo')
        tasks = Task.objects.all()
        filter_backend = SearchFilter()
        search_fields = ['title', 'description']  # Specify the fields to search on

    # Apply search filtering
        filtered_queryset = filter_backend.filter_queryset(request, tasks, view= None)
    
        serializer = TaskSerializer(filtered_queryset, many=True)
        #serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
def task_create(request):
    if request.user.has_perm('task.add_task'):
        
                             
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    else:
        raise PermissionDenied("You do not have permission to access this resource.")

    

@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['PUT'])
@login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def task_delete(request, pk):
   print('oooooooo')
   try:
        task = Task.objects.get(pk=pk)
        
        # Check if the user has permission to delete the task
        if not request.user.has_perm('tasks.can_delete_task'):
            return HttpResponseForbidden("You are not authorized to delete this task.")
        
        task.delete()
        return HttpResponse("Task deleted successfully.")
   except Task.DoesNotExist:
       return HttpResponseNotFound("Task not found.")

##comment_views 


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated ,ISDIRECTOR])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


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
    tasks = Task.objects.prefetch_related('comment_set').all()
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
