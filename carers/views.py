from django.shortcuts import render, redirect
from .forms import CarerForm

# Create your views here.


def carer_profile(request):
    """View to add carer's details"""
    if request.method == "POST":
        form = CarerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = CarerForm()
    return render(request, "add_carer.html", {'form': form})

def thanks(request):
    """View to render thank you page"""
    return render(request, 'thanks.html')
