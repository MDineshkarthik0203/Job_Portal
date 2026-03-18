from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL
class Job(models.Model):
    company_name=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=100)
    salary=models.IntegerField()
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    