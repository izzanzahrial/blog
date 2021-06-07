from accounts.models import Profile
from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import fields

# https://docs.djangoproject.com/en/3.0/topics/auth/default/
# https://docs.djangoproject.com/en/3.0/topics/forums/

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 
        'placeholder': 'Username', 
        'id': 'login-username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'id': 'login-pwd',
        }
    ))

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Email is required!'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-3", "placeholder": "E-mail", "name": "email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Repeat Password"}),
        }

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exist")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exist")
        return email

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("Password doesn't match")
        return password2

class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "email", "id": "form-email"}))

    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError("Cannot find the email")
        return email

class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-newpass"}))
    new_password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-new-pass2"}))

class UserEditForm(forms.ModelForm):
    
    first_name = forms.CharField(label="Firstname", min_length=4, max_length=50, required=False, widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Firstname",
        "id": "form-firstname",
    }))

    last_name = forms.CharField(label="Lastname", min_length=4, max_length=50, required=False, widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Lastname",
        "id": "form-lastname",
    }))

    email = forms.EmailField(max_length=255, required=False, widget=forms.TextInput(attrs={
        "class": "form-control mb-3",
        "placeholder": "Email",
        "id": "form-email",
    }))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False

class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
    }))

    class Meta:
        model = Profile
        fields = ['bio']

class PwdChangeForm(PasswordChangeForm):

    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3", 
        "placeholder": "Old Password",
        "id": "form-oldpass",
    }))

    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3", 
        "placeholder": "New Password",
        "id": "form-newpass",
    }))

    new_password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={
        "class": "form-control mb-3", 
        "placeholder": "Repeat Password",
        "id": "form-newpass2",
    }))