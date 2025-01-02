from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def api_home(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World"})
