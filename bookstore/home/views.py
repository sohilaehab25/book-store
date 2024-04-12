from django.shortcuts import render
from books.models import Book
from category.models import Category
from home.forms import BookSearchForm
from books.models import Tag


from django.shortcuts import get_object_or_404

def get_home(req):
    form = BookSearchForm()
    search_results = []

    latest_books = Book.objects.order_by('-created_at')[:5]
    highest_priced_books = Book.objects.order_by('-price')[:5]
    latest_categories = Category.objects.order_by('-created_at')[:2]
    featured_books = Book.objects.filter(featured=True).order_by('-created_at')[:5]
    
    query = req.GET.get('query')
    category = None
    
    if query:
        category_results = Category.objects.filter(name__icontains=query)
        if category_results.exists():
            category = category_results.first() 
            search_results = Book.objects.filter(category=category)
        else:
            search_results = Book.objects.filter(tag__name__icontains=query)
    
    return render(req, "home/index.html", context={"featured_books": featured_books,"books": latest_books, "categories": latest_categories, "highest_priced_books": highest_priced_books, 'form': form, "search_results":search_results, "category": category})



