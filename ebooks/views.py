from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'ebooks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')





@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Книга успешно добавлена!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'ebooks/add_book.html', {'form': form, 'form_title': 'Добавление книги'})

@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Книга успешно обновлена!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'ebooks/edit_book.html', {'form': form, 'form_title': 'Редактирование книги'})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Книга успешно удалена!')
        return redirect('book_list')
    return render(request, 'ebooks/delete_book.html', {'book': book})