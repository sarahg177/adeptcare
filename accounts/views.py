from django.shortcuts import render, redirect, reverse

# Create your views here.


def welcome(request):
    """Return the welcome.html file"""
    return render(request, 'welcome.html')


def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('welcome'))
