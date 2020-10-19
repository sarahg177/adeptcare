from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.


def welcome(request):
    """Return the welcome.html file"""
    return render(request, 'welcome.html')


def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success((request, "You have successfully been logged off"))
    return redirect(reverse('welcome'))


def login(request):
    """Return a login page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('carer_list'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
        return render(request, 'login.html', {"login_form": login_form})


def register(request):
    """Render the registration page"""
    registration_form = UserRegistrationForm()
    if request.user.is_authenticated:
        return redirect(reverse('logout'))
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user=user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
        else:
            messages.error(request, "Unable to register your account at this time")

    return render(request, 'register.html', {'registration_form': registration_form})
