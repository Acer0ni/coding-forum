from django.db import models
from django.db.models.deletion import CASCADE
from api.models import User

class Thread(models.Model):
    author = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    original_post = models.CharField(max_length=500)
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=50)