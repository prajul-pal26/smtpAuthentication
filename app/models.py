from django.db import models
from django.contrib.auth.models import User   # used for inbuild authentication
# Create your models here.

# class Student(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
#     #we use foreign key because if we delete that user then the data related to that is also be deleted 
#     name = models.CharField(max_length=100, null=True, blank=True)
    