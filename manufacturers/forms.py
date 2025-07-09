from django import forms
from .models import EstablishmentProfile

class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = EstablishmentProfile
        fields = '__all__'