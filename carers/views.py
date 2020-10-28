from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import CarerForm
from carers.models import Carer

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


def get_carer_list(request):
    """View to show list of all carers"""
    all_carers = Carer.objects.all()
    return render(request, "view_carer_list.html", {'carers': all_carers})


class CarerDetailView(DetailView):
    model = Carer
    template_name = 'carer_detail.html'