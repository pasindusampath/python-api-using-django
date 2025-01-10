from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Student
import json;

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
    try:
        data = json.loads(request.body)
        student = Student.objects.create(
            name = data["name"],
            age = data["age"],
            email = data["email"],
        )
        return JsonResponse({"id":student.id},status = 201)
    except KeyError as e:
        return JsonResponse({"error missing field : ":str(e)})
    except Exception as e:
        return JsonResponse({"error":str(e)})

def api_patch(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from patch"})

def api_delete(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from delete"})

def api_put(request,*args, **kwargs):
    return JsonResponse({"message":"Hello World from put"})

def api_get(request,*args, **kwargs):
    id = request.GET.get("id")
    if(id):
        try:
            student = Student.objects.get(id = id)
            return JsonResponse({
                "id":student.id,
                "name":student.name,
                "age":student.age,
                "email":student.email,
                "created_at":student.created_at,
                "updated_at":student.updated_at,
            })
        except Exception as e:
            return JsonResponse({"error":str(e)})
    return JsonResponse({"message":"Hello World from get"})
