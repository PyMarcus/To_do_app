from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Task


def index(request: HttpRequest) -> HttpResponse:
    task = Task.objects.all()
    print(task)
    if request.method == 'POST':
        if request.POST.get('addtext', False):
            new_item = Task.objects.create(text=request.POST.get('addtext'))
            new_item.save()
        else:
            Task.objects.filter(text=list(request.POST.values())[1]).delete()
    content = {
        "text": task,
    }
    return render(request, "index.html", content)
