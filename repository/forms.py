from django import forms
from django.forms.forms import Form

class ContactForm(forms.Form):
    name = forms.CharField(required=True, help_text='Required', error_messages={'required': 'Your Name is required'}, widget=forms.TextInput(attrs={
        "class": "field",
        "placeholder": "Your Name"
    }))
    email = forms.EmailField(required=True, help_text='Required', error_messages={'required': 'Your Email is required'}, widget=forms.TextInput(attrs={
        "class": "field",
        "placeholder": "Your Email"
    }))
    message = forms.CharField(required=True, help_text='Required', error_messages={'required': 'Say something to me'}, widget=forms.Textarea(attrs={
        "class": "field",
        "placeholder": "Message",
        "cols": 30,
        "rows": 10
    }))