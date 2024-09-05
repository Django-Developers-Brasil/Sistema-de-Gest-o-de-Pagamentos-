from django.shortcuts import render, HttpResponse

def exemple_view(request):
    return HttpResponse('OK')
