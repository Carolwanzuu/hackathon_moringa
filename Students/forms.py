from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GroupForm(forms.ModelForm):
    class Meta:
        model = chamaGroup
        fields = ('name', 'description', 'amount')

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'chamagroup')


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['reply']