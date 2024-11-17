from django.db import models
from .user import User
from .assignment import Assignment
class Subtask (models.Model):
    title = models.CharField(max_length=10)
    asgn=models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="parent_assignment")
    text= models.TextField()
    def __str__(self):
        return self.title