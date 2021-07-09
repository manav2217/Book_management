from django import  forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['b_name' , 'b_author' , 'b_genre' , 'b_language']