from django import forms
from .models import Vlogs

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Vlogs
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }