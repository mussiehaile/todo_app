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

class TaskSerializer(serializers.ModelSerializer):
    duedate_set = DueDateSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
