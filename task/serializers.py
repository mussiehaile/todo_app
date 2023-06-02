from rest_framework import serializers
from .models import Task, DueDate, Comment
from account.serializers import UserAccountSerializers
class DueDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DueDate
        fields = ['task','due_date']
      
class TasksSerializer(serializers.ModelSerializer):
    duedate_set = DueDateSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'duedate_set']
        #fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    task = TasksSerializer(read_only=True)
    user = UserAccountSerializers()
    class Meta:
        model = Comment 
        fields = ['id', 'comment', 'created_at', 'task', 'user']
        read_only_fields = ('created_at',)
        

class TaskSerializer(serializers.ModelSerializer):
    duedate_set = DueDateSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'duedate_set', 'comment_set']
        #fields = '__all__'



    
    
        
    
    
        


