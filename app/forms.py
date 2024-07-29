from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ('Name', 'Subject', 'Email', 'Message')

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Message': forms.Textarea(attrs={'class': 'form-control'})
        }