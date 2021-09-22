from django import forms


class UserLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
            "name": "username",
            "placeholder": "Username"
        }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "name": "password",
            "placeholder": "Password"
        }))
