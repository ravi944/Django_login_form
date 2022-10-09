from django import forms
from django.contrib.auth.models import User


class RegForm(forms.Form):
	Name = forms.CharField(label='Your name', max_length=200, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'E.g. Akshat'}))
	your_email = forms.EmailField( label='Email',max_length=200, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'E.g. Akshat@techbrise.com'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'form-control'}))
	Phone = forms.CharField( label ='What is the best number to reach you at?' , max_length=12, widget=forms.TextInput(attrs={ 'class':'form-control Phone', 'placeholder':'E.g.: +91 9563254568'}))

class LoginForm(forms.Form):
	your_email = forms.EmailField( label='Email',max_length=200, widget=forms.TextInput(attrs={ 'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'form-control'}))