"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))




class AddWrestlerForm(forms.Form):
    name = forms.CharField(label='Name: ', max_length=80, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))

class EditWrestlerForm(forms.Form):
    old_name = forms.ModelChoiceField(queryset=Wrestler.objects.all().order_by('name'), empty_label=None)
    new_name = forms.CharField(label='New Name: ', max_length=80, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'John Doe'}))

class DeleteWrestlerForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Wrestler.objects.all().order_by('name'), empty_label=None)

class ViewWrestlerForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Wrestler.objects.all().order_by('name'), empty_label=None)