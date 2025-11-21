from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    
    class Meta:
        model = Equipamento

        fields = [
            'nome',
            'numero_serie',
            'data_aquisicao',
            'categoria',
            'status'
        ]
        widgets = {
            'data_aquisicao': forms.DateInput(attrs={'type': 'date'}),
            }