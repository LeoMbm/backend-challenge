from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm


# Create your views here.
def getHome(request):
    ctx = {'message': "home"}
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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('/users/')
        else:
            return redirect('/users/registration/')
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('/users/')


def error_404_view(request, exception):
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, 'error_404.html')