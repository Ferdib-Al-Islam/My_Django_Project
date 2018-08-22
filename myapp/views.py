from django.shortcuts import render
from django.http import HttpResponse
from .models import List


def home(request):
    return HttpResponse('Hello, World!')

def first(request):
    data = List.objects.all()
    #return HttpResponse(data)
    return render(request, 'show_project.html', {'data':data})

