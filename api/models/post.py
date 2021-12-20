from django.db import models
from api.models import User
from api.models.thread import Thread

class Post(models.Model):
    author = models.ForeignKey(User,related_name="author",on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread,related_name="thread",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    