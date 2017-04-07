from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
        class Meta:
                model = User
                fields = ['username', 'email', 'password']
