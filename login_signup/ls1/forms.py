
from django import forms
from .models import superuser

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number'}))
    role = forms.ChoiceField(choices=superuser.ROLE_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = superuser
        fields = ['username', 'email', 'phone', 'role', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match")

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))
