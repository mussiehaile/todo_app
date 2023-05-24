from rest_framework.decorators import api_view ,permission_classes 
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated ,AllowAny
from rest_framework.response import Response
from .models import Comment,Task ,DueDate
from .serializers import TaskSerializer,CommentSerializer ,DueDateSerializer


## task view
@api_view(['GET'])
@permission_classes([AllowAny])
def task_list(request):
    
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response(status=204)

##comment_views 

@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
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
