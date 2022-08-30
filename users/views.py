from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def getHome(request):
    ctx = {'message': "hello world"}
    return JsonResponse(ctx)
