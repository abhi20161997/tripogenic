from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm):

	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['first_name', 'email', 'password',"username"]

class AuthenticateForm(AuthenticationForm):
	username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

	def is_valid(self):
		form = super(AuthenticateForm, self).is_valid()
		for f, error in self.errors.iteritems():
			if f != '__all__':
				self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
		return form