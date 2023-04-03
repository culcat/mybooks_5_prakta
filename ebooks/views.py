from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'ebooks/book_list.html', {'books': books})

def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    file_path = book.pdf_file.path
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=' + book.pdf_file.name
        return response

def book_detail(request, pk):
        book = get_object_or_404(Book, pk=pk)
        context = {
            'book': book
        }
        return render(request, 'ebooks/book_detail.html', context)