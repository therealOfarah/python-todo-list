from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Importance(models.Model):
  level = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
      )
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("genre_detail", kwargs={"pk": self.id})


class Todo(models.Model):
  task= models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  importance= models.ManyToManyField(Importance)
  user=models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
  return self.show
