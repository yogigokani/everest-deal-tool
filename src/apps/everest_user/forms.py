from django import forms


class LoginForm(forms.Form):
    email_id = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
