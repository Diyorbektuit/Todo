from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    datetime = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Todo of {self.user.username}"
