from django.urls import path
from home.views import *
 
urlpatterns = [
    path('',  get_home,name='home.get'),
        ]
