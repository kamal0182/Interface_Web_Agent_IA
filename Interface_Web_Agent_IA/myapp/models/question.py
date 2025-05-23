from django.db import models
class Question (Models.Model) 
    content = models.TextField() 
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions');