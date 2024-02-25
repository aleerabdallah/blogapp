from django import forms
from django.utils.html import html_safe
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CommentForm(forms.Form):
	name = forms.CharField(max_length=100, label="Name")
	email = forms.EmailField(label="Email")
	body = forms.CharField(label="Comment", widget=forms.Textarea)



class RegisterForm(forms.Form):
	username = forms.CharField(label="Username", max_length=30, min_length=5)
	email = forms.EmailField(label="Email")
	password = forms.CharField(label="Password", min_length=6, max_length=255, widget=forms.PasswordInput)
	password2 = forms.CharField( label="Confirm your password", min_length=6, max_length=255, widget=forms.PasswordInput)

	class Media:
		css = {'all': ('play/css/registerform.css',),}
		js = []


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	class Media:
		css = {'all': ('play/css/login.css',),}
		js = []