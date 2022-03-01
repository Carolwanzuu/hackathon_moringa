from django import forms
from .models import *

class GroupForm(forms.ModelForm):
    class Meta:
        model = chamaGroup
        fields = ('name', 'description', 'amount')