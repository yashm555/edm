from django import forms
from django.conf import settings
from .models import *

class CustomerForm(forms.ModelForm):
    CustomerId    = forms.IntegerField()
    CustomerName  = forms.CharField(max_length=10)

    class Meta:
        model = Customer
        fields = '__all__'
