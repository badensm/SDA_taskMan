from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(blank=True,null=True)
    importance = models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} | {self.title}'