from django import forms
from .models import Snock


class SnockForm(forms.ModelForm):
    class Meta:
        model = Snock
        fields = ['ticker'] 