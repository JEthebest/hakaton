from django import forms
from tickets.models import Pnr

class PnrForm(forms.ModelForm):
    class Meta:
        model = Pnr
        fields = ['code']
        labels = {'code': 'PNR код'}
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%'}),
        }