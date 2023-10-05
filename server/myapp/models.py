from django.db import models
from django.contrib.auth.models import AbstractUser

class Question(models.Model):
    question_number = models.IntegerField(null=True,blank=True,default=None)
    name = models.CharField(null=True,blank=True,default=None,max_length=225)
    answer = models.CharField(null=True,blank=True,default=None,max_length=225)
    description = models.CharField(null=True,blank=True,default=None,max_length=225)
    imgpath = models.CharField(null=True, blank=True, default=None, max_length=255)
    def __str__(self):
        return self.name

class User(AbstractUser):
    remaining_questions = models.ManyToManyField(Question)
    score = models.IntegerField(default=0, blank=True, null=True)