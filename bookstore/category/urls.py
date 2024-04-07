from django.urls import path
from category.views import *

urlpatterns = [
    path('helloworld/', hello, name="hellopage"),
    path('welcomeso/', welcome, name="welcome"),
    path('home', home, name='categories.home'),
    path('create', create_category, name='categories.create'),
    path('', categories_index, name='categories.index'),
    path('<int:id>', category_show, name='categories.show'),
    path('delete/<int:id>/', category_delete, name='categories.delete'),
    path('update<int:id>',  category_updated,name='categories.update')
        ]
