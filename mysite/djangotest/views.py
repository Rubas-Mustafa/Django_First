from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import ToDoList, Items 
from .forms import CreateNewList

# appearance of website
# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.usertodolist.all():
        if response.method == 'POST':
            print(response.POST)
            if response.POST.get('save'):
                for item in ls.items_set.all():
                    if response.POST.get('c' + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get('newItem'):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.items_set.create(text=txt, complete=False)
        return render(response, "djangotest/list.html", {"ls" : ls})
    return render(response, "djangotest/view.html", {})

def home(response):
    return render(response, "djangotest/home.html", {})

def create(response):
    response.user
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add.create(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()

    return render(response, "djangotest/create.html", {"form" : form })

def view(response):
    return render(response, "djangotest/view.html", {})