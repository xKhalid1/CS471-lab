from django import forms
from django.db import models

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book # tell form that model to map 
        fields = ['title', 'author', 'edition', 'price'] # tell form what to map from model 
    title = forms.CharField( 
        max_length=100, 
        required=True, 
        label="Title",
        widget= forms.TextInput( attrs= { 
            'placeholder':'', 
            'class':"mycssclass", 
            'id':'jsID'
            }))
    author = forms.CharField(
        max_length=100, 
        required=True, 
        label="Author",
        widget= forms.TextInput( attrs= { 
            'placeholder':'', 
            'class':"mycssclass", 
            'id':'jsID'
            }))
    edition = forms.IntegerField(
        required=True, 
        initial=0, 
        widget=forms.NumberInput()
        )
    price = forms.DecimalField(
        required=True, 
        label="Price", 
        initial=0
        ) 

    
    
