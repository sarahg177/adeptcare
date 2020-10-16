from django.shortcuts import render
from .forms import CarerForm

# Create your views here.


def carer_profile(request):
    """View to add carer's details"""
    if request.method == "POST":
        form = CarerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CarerForm()
    return render(request, "add_carer.html", {'form': form})
