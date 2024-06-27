from django import forms
from .models import *

class CelularForm(forms.ModelForm):
    class Meta:
        model = Celulares
        fields = ['modelo', 'ano_fabricacao']
        exclude = ['outro_campo']