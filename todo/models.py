from django.db import models
from django.utils import timezone
# Create your models here.
class todoMain(models.Model):
    todo_title = models.CharField(max_length=125)
    todo_status = models.BooleanField(default=False)
    todo_creation_Date = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.todo_title

class todoItem(models.Model):
    todo_item_text = models.CharField(max_length=150)
    todo_item_status = models.BooleanField(default=False)
    todo_item_duedate = models.DateTimeField(blank=True, null=True)
    todo_item_completion = models.DateTimeField(blank=True, null=True)
    todo_item_from = models.ForeignKey(todoMain, on_delete=models.CASCADE)
    def __str__(self):
        return self.todo_item_text