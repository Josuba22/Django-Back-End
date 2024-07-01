from django import forms
from .models import *

class FormularioLead(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'