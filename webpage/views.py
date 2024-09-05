from django.shortcuts import render, HttpResponse

def example_view(request):
    return HttpResponse('OK')
