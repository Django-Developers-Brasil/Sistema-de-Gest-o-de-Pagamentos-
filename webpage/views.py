from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('OK')

def Error(request):
    return render(request,'404.html')

def index(request):
    return render(request,'index.html')


def terms_of_service(request):
    return render(request, 'terms_of_service.html')



