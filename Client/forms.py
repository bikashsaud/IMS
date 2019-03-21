from .models import Client
from django.forms import ModelForm
from django import forms
from Agent.models import Agent
class ClientForm(forms.ModelForm):
    class Meta:
        """docstring for Meta"""
        model=Client
        fields='__all__'
class ClientLoginForm(forms.ModelForm):
    class Meta:
        model=Client
        fields=['Email','Form_number']

class AgentForm(forms.ModelForm):
    class Meta:
        """docstring for Meta"""
        model=Agent
        fields='__all__'
class AgentLoginForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields=['Email','License_code']
