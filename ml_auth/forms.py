from django import forms
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    """Login form for the application."""

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Username'),
               'class': 'form-control input-lg',
               'autofocus': 'true'}),
        error_messages={'required': 'Please enter your username.'})

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': _('Password'),
               'class': 'form-control input-lg',
               'autofocus': 'true'}),
        error_messages={'required': 'Please enter your password.',
                        'invalid': 'Please enter a valid password.'},)

    def clean_username(self):
        """Method to clean username."""
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError("Please enter your username.")
        return username

    def clean_password(self):
        """Method to clean password."""
        password = self.cleaned_data['password']
        if not password:
            raise forms.ValidationError("Please enter your password.")
        return password
