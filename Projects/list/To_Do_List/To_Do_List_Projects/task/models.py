from django.contrib.auth.models import User
from django.db import models

class Task (models.Model):
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

