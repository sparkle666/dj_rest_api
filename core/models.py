from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField

User = get_user_model() # Gets the current user

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title