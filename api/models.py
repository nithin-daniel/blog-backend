from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    blog_author = models.ForeignKey(User,on_delete=models.CASCADE)