from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('OK')

def Error(request):
    return render(request,'404.html')
