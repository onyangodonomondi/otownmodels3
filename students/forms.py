from django import forms 
from .models import Student
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['phone_number', 'first_name', 'last_name', 'email']
    labels = {
      'phone_number': 'phone Number', 
      'first_name': 'First Name', 
      'last_name': 'Last Name', 
      'email': 'Email', 
      
    }
    widgets = {
      'phone_number': forms.NumberInput(attrs={'class': 'form-control'}), 
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      
    }