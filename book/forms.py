from django import forms
from django.forms import Form
from book.models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
           "author":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
           "genre":forms.TextInput(attrs={"class":"form-control"}),

        }