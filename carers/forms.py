from django import forms
from .models import Carer


class CarerForm(forms.ModelForm):
    class Meta:
        model = Carer
        fields = ('first_name', 'last_name', 'known_as', 'telephone', 'email', 'short_bio', 'image')

