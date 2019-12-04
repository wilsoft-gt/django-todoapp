from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolistview, name='todolist'),
    path('item', views.todoitemview, name='todoitem' ),
    path('deleteitem', views.deleteitem, name='deleteitem'),
    path('update', views.updateitem, name='update')
]