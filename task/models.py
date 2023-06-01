from django.db import models
from account.models import UserAccount

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 
    


class DueDate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    due_date = models.DateTimeField()


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
