from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODOLIST(models.Model):
    sr = models.AutoField(primary_key=True,auto_created=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add=True)

