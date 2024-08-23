from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(
        request,
        "todos/home.html",
    )

# /home/aluno/Documentos/vspaul/todos/template/todos/home.html
# todos/template/todos/home.html