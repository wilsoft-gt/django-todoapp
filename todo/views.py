from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import todoMain, todoItem
# Create your views here.


def reverse(item):
    if True:
        return False
    else:
        return True


def todolistview(request):
    if request.method == "POST":
        data = request.POST["taskname"]
        newtodomain = todoMain()
        newtodomain.todo_title = data
        newtodomain.save()
        lista = todoMain.objects.all()
        return render(request, 'todo/todolist.html', {'lista': lista})
    else:
        lista = todoMain.objects.all()
        return render(request, 'todo/todolist.html', {'lista': lista})


def todoitemview(request):
    if request.method == "POST":
        mainList = request.POST["mainid"]
        attachedtomain = todoMain.objects.get(id=mainList)
        taskname = request.POST["taskname"]
        newtask = todoItem()
        newtask.todo_item_text = taskname
        newtask.todo_item_from = attachedtomain
        newtask.save()

        #verificar si los tasks estan finalizados prar cambiar el estado
        toquery = todoItem.objects.all().filter(todo_item_from=mainList)
        mainListTasksStatus = list(map(lambda x: toquery[x].todo_item_status, range(len(toquery))))
        print(list(mainListTasksStatus))
        if False in mainListTasksStatus:
            print ("Aun hay falsos en la lista")
            updatemainliststatus = todoMain.objects.get(id=mainList)
            updatemainliststatus.todo_status = False
            updatemainliststatus.save()
        else:
            print ("La lista esta completa")
            updatemainliststatus = todoMain.objects.get(id=mainList)
            updatemainliststatus.todo_status = True
            updatemainliststatus.save()

        return HttpResponseRedirect("item?id="+mainList)
    else:
        listmainid = request.GET.get("id")
        maintitle = todoMain.objects.get(id=listmainid)
        listitems = todoItem.objects.all().filter(todo_item_from=listmainid)
        return render(request, 'todo/todoitem.html', {'listmainid': maintitle, "listitems": listitems})


def deleteitem(request):
    data = request.GET.get("data")
    todelete = request.GET.get("id")
    idmain = request.GET.get("idmain")
    if data == "item":
        deleted = todoItem.objects.get(id=todelete)
        deleted.delete()
        return HttpResponseRedirect("item?id="+idmain)
    if data == "list":
        deleted = todoMain.objects.get(id=idmain)
        deleted.delete()
        return HttpResponseRedirect("/")


def updateitem(request):
    toupdate = request.GET.get("update")
    mainList = request.GET.get("id")
    item = todoItem.objects.get(id=toupdate)

    if item.todo_item_status == True:
        item.todo_item_status = False
        item.save()
        toquery = todoItem.objects.all().filter(todo_item_from=mainList)
        mainListTasksStatus = list(map(lambda x: toquery[x].todo_item_status, range(len(toquery))))
        print(list(mainListTasksStatus))
        if False in mainListTasksStatus:
            print ("Aun hay falsos en la lista")
            updatemainliststatus = todoMain.objects.get(id=mainList)
            updatemainliststatus.todo_status = False
            updatemainliststatus.save()
        else:
            print ("La lista esta completa")
            updatemainliststatus = todoMain.objects.get(id=mainList)
            updatemainliststatus.todo_status = True
            updatemainliststatus.save()
    else:
        item.todo_item_status = True
        item.save()
        toquery = todoItem.objects.all().filter(todo_item_from=mainList)
        mainListTasksStatus = list(map(lambda x: toquery[x].todo_item_status, range(len(toquery))))
        print(list(mainListTasksStatus))
        if False in mainListTasksStatus:
            print ("Aun hay falsos en la lista")
            updatemainliststatus = todoMain.objects.get(id=mainList)
            updatemainliststatus.todo_status = False
            updatemainliststatus.save()
        else:
            print ("La lista esta completa")
            updatemainliststatus = todoMain.objects.get(id=mainList)
            updatemainliststatus.todo_status = True
            updatemainliststatus.save()
    return HttpResponseRedirect("item?id="+mainList)
