from django.shortcuts import render
from django.http import HttpResponse


def msg(request):
    context = {
        "msg": "Hello World!",
    }
    return render(request, 'msg.html', context)
