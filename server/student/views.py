from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
@csrf_exempt
def api_home(request,*args, **kwargs):
    print(request.method)
    if(request.method == "POST"):
        return api_post(request,*args, **kwargs)
    elif(request.method == "PATCH"):
        return api_patch(request,*args, **kwargs)
    elif(request.method == "DELETE"):
        return api_delete(request,*args, **kwargs)
    elif(request.method == "PUT"):
        return api_put(request,*args, **kwargs)
    elif(request.method == "GET"):
        return api_get(request,*args, **kwargs)

def api_post(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from post"})

def api_patch(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from patch"})

def api_delete(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from delete"})

def api_put(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from put"})

def api_get(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from get"})
