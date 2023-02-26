from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


items = ["Estudar python",
         "Colocar ração para o cachorro",
         "jogar video-game"]


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if request.POST.get('addtext', False):
            items.append(request.POST.get('addtext', False))
        else:
            del items[int(list(request.POST.keys())[1]) - 1]
    content = {
        "text": items,
    }
    return render(request, "index.html", content)
