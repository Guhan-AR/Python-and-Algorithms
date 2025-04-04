from django.shortcuts import render, redirect
from .forms import *
from .models import *

def index(request):
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'index.html',context)

def add_book(request):
    context = {
        'book_form': Book_Form()
    }

    if request.method == 'POST':
        book_form = Book_Form(request.POST , request.FILES)
        if book_form.is_valid():
            print("Yes this is a valid field to save in database.")
            book_form.save()
    return render(request, 'adding_books.html', context)

def delete_book(request,id):
    print('*'*20)
    print(id)
    print('*'*20)
    selected_book = Book.objects.get(id=id)
    print(selected_book)
    print('#'*20)
    selected_book.delete()
    return redirect('/')