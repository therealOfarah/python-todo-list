from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Todo(models.Model):
  task= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  level = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
      )
  color = models.CharField(max_length=20) 
  user=models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:
  ordering = ['-level']
