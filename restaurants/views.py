from django.shortcuts import render
from django.http import HttpResponse


def task2(request):
    context = {
        "msg": "Hello world",
    }
    return render(request, 'msg.html', context)
