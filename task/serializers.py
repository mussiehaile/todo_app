from rest_framework import serializers
from .models import Task, DueDate, Comment

class DueDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DueDate
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'created_at', 'task', 'user']
        read_only_fields = ('created_at',)
    
    def get_task(self, obj):
        return f"{obj.task.title} - {obj.task.description}"
        
    
    
        

class TaskSerializer(serializers.ModelSerializer):
    duedate_set = DueDateSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
   
    class Meta:
        model = Task
        fields = ['id','title','description','duedate_set','comment_set']

