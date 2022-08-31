from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm


# Create your views here.
def getHome(request):
    ctx = {'message': "registration"}
    return render(request, 'home.html', ctx)


def registerPage(request):
    ctx = {'message': "User created"}
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('/users/')
    else:
        form = RegistrationForm()
    return render(request, "registration.html", {"form": form, "message": 'Registration'})


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, email)
            redirect('/users/')
    return render(request, "login.html")
