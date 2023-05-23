from rest_framework import serializers
from .models import Task, DueDate, Comment

class DueDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DueDate
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at',)

class TaskSerializer(serializers.ModelSerializer):
    #comments = CommentSerializer(many= True)
    duedate_set = DueDateSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
   
    class Meta:
        model = Task
        fields = ['id','title','description','duedate_set','comment_set']
