from django import forms
from .models import Devtool


class DevtoolForm(forms.ModelForm):
    class Meta:
        model = Devtool
        fields = ['name', 'kind', 'content']
