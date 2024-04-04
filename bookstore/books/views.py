from django.shortcuts import render, get_object_or_404,reverse,redirect
from django.http import HttpResponse


import json


from books.models import Book





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
     

def book_updated(req, id):
    book = get_object_or_404(Book, pk=id)
    
    if req.method == 'POST':
        book.name = req.POST.get('name', book.name)
        book.price = req.POST.get('price', book.price)
        if req.FILES:
            book.image = req.FILES['image']
        book.save()
        return redirect('books.books_index')
    
    return render(req, 'books/crud/update.html', {'book': book})