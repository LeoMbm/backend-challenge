from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def getHome(request):
    ctx = {'message': "registration"}
    return render(request, 'registration.html', ctx)
