from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Python Django is the best')