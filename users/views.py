from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from users.forms import RegistrationForm


# Create your views here.
def getHome(request):
    ctx = {'message': "registration"}
    return render(request, 'registration.html', ctx)


def register(request):
    ctx = {'message': "User created"}
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form, "message": 'Registration'})
