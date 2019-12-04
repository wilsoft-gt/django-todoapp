from django.contrib import admin
from .models import todoItem, todoMain
# Register your models here.
class todomainadmin(admin.ModelAdmin):
    list_display = ('todo_title', 'todo_creation_Date')
admin.site.register(todoMain, todomainadmin)

class todoitemadmin(admin.ModelAdmin):
    list_display = ('todo_item_text', 'todo_item_from', "todo_item_duedate")
admin.site.register(todoItem, todoitemadmin)