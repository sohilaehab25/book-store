from django.shortcuts import render, redirect, reverse
# Create your views here.


def profile_view(request):
    return redirect('books.books_index')
