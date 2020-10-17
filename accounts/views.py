from django.contrib import auth, messages
from django.shortcuts import render, redirect, reverse
from .forms import UserLoginForm

# Create your views here.


def welcome(request):
    """Return the welcome.html file"""
    return render(request, 'welcome.html')


def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('welcome'))


def login(request):
    """Return a login page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")
            if user:
                auth.login(user=user, request=request)
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm(),
        return render(request, 'login.html', {"login_form": login_form})
