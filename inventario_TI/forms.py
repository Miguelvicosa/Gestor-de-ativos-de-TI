from django import forms
from .models import Equipamentos

class EquipamentoForm(forms.ModelForm):
    
    class Meta:
        model = Equipamentos

        fields = [
            'nome',
            'numero_serie'
            'cor'
            'data_aquisicao'
            'categoria'
            'status'
        ]
