from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover_image', 'pdf_file']

class DeleteBookForm(forms.Form):
    book_id = forms.IntegerField()

class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover_image', 'pdf_file']
