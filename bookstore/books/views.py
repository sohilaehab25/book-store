from django.shortcuts import render, get_object_or_404,reverse,redirect
from django.http import HttpResponse
from books.models import Book
from books.modelform import BookModelForm
from books.modelform import Tag
from books.modelform import TagForm
from category.models import Category
from django.contrib.auth.decorators import login_required



import json







# Create your views here.

def hello(req):
    print (req)
    return HttpResponse('we are here')

def welcome(req):
    print(req)
    return HttpResponse("hello soso")

# books =[
#     {'id':1, 'name':'story1', 'price':'104 LE','image':"1.jpg"},
#     {'id':2, 'name':'story2', 'price':'10 LE','image':"2.jpg"},
#     {'id':3, 'name':'story3', 'price':'400 LE','image':"3.jpg"},
#     {'id':4, 'name':'story4', 'price':'300 LE','image':"1.jpg"},
#     {'id':5, 'name':'story5', 'price':'100 LE','image':"1.jpg"}
# ]

def getallbooks(req):
    print (req)
    return HttpResponse(Book)


def getbookbyid(req, id):
    book_list = filter(lambda book: book['id'] == id, books)
    allbooks = list(book_list)
    if allbooks:
        book = allbooks[0]
        return render(req, "books/detailes.html", context={"book": book})

def home(request):
    return render(request, "books/home.html",
                  context = {"books": books},
                  status=200)  # render http response
    
def contactus(req):
    return render(req, "books/contactus.html",status=200)    
def aboutus(req):
    return render(req, "books/aboutus.html",status=200)    
    
    
def books_index(req):
     books  = Book.objects.all()
     return render(req, "books/index.html",
                  context={"books": books})
 
def show_index(req,id):
    book = get_object_or_404(Book, pk=id)
    # book=Book.objects.get(id=id)
    return render(req, "books/crud/show.html", context={"book": book})


def book_delete(req, id):
    book = get_object_or_404(Book, pk=id)
    book.delete()
    # return HttpResponse("produc deleted")
    url = reverse("books.books_index")
    return redirect(url)
    
def book_create(req):
    # print(request)
    if req.method == "POST":
        # print(request.POST)
         print(req.FILES)
         if req.FILES:
            image = req.FILES["image"]
         else:
            image = None
         book_ = Book(name=req.POST["name"], price=req.POST["price"], image=image)
         book_.save()
         url = reverse("books.books_index")
         return redirect(url)
        #  return HttpResponse("Post request received")
       # get request
    return  render(req, 'books/crud/create.html')
     
@login_required
def book_updated(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookModelForm(instance=book)
    
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.books_index')
    
    return render(request, 'books/crud/update.html', {'form': form})
@login_required
def create_bookform(request):
    form = BookModelForm()
    if request.method == "POST":
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category']
            tag_name = form.cleaned_data['tag']
            category, created = Category.objects.get_or_create(name=category_name)
            tag, created = Tag.objects.get_or_create(name=tag_name)
           

            book = form.save(commit=False)
            book.category = category
            book.tag = tag
            book.save()

            return redirect(book.show_url)

    return render(request, 'books/forms/createbookform.html', {'form': form})


def tag_index(request):
    tags = Tag.objects.all() 
    return render(request, 'tags/index.html', {'tags': tags})


@login_required
def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.tag_index')  
    else:
        form = TagForm()
    return render(request, 'tags/create_tag.html', {'form': form})