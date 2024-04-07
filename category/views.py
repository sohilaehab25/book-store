from django.shortcuts import render, get_object_or_404,reverse,redirect
from django.http import HttpResponse
from category.models import Category
from category.form import CategoryModelForm


# Create your views here.
def hello(req):
    print (req)
    return HttpResponse('we are here')

def welcome(req):
    print(req)
    return HttpResponse("hello soso")

def home(req):
    return render(req, "categories/index.html")


def categories_index(request):
    categories = Category.get_all_categories() 
    return render(request, 'categories/index.html', {'categories': categories})

def create_category(request):
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect('categories.index')
    return render(request, 'categories/create.html', {'form': form})



def category_show(req, id):
    category = Category.get_category_byid(id)
    return render(req, 'categories/show.html', {'category' : category})


def category_delete(req, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    url = reverse("categories.index")
    return redirect(url)
    
def category_updated(req, id):
    category = get_object_or_404(Category, pk=id)
    
    if req.method == 'POST':
        category.name = req.POST.get('name', Category.name)
        category.description = req.POST.get('description', Category.description)
        if req.FILES:
            category.logo = req.FILES['logo']
        category.save()
        return redirect('categories.index')
    
    return render(req, 'categories/update.html', {'category': category})
