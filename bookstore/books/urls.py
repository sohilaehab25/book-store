from django.urls import path
from books.views import *
        

urlpatterns = [
    path('helloworld/',hello,name="hellopage" ),
    path('welcomeso/',welcome,name = "welcome" ),
    path('land/', getallbooks, name='land'),
    path('old/<int:id>', getbookbyid, name='books.getbookbyid'),
    path('home/', home, name='books.home'),
    path('aboutus/', aboutus,name='books.aboutus'),
    path('contactus/', contactus,name='books.contactus'),
    path('', books_index,name='books.books_index'),
    path('<int:id>', show_index, name='books.show_index'),
    path('<int:id>/delete', book_delete, name='books.delete'),
    path('create_book', book_create,name='books.create'),
    path('<int:id>/update',book_updated,name='books.book_updated')

]
