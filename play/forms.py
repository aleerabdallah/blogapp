from django import forms
from django.utils.html import html_safe
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . models import Task


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


@html_safe
class CssPath:
	def __str__(self):
		return '<link rel="stylesheet" href="static/play/css/form.css">'

class NameForm(forms.Form):
	first_name = forms.CharField(min_length=6, max_length=12, label="First Name", label_suffix="*")
	last_name = forms.CharField(min_length=6, max_length=12, label="Last Name", label_suffix="*")
	url = forms.URLField()

	def clean_url(self):
		data = self.cleaned_data.get('url')
		if 'www.' in data:
			return data
		elif 'https://' in data:
			return data
		else:
			raise ValidationError("Enter a complete url")

	def clean(self):
		cleaned_data = super().clean()
		first_name = cleaned_data.get('first_name')
		last_name = cleaned_data.get('last_name')

		if last_name == first_name:
			msg = "First name and Last name cannot be the same."
			self.add_error('last_name', msg)
		else:
			pass


class AddToDo(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'completed']



class LoginForm(forms.Form):
	username = forms.CharField(max_length=100, label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)

	class Media:
		css = {'all': ('play/css/login.css',),}
		js = []