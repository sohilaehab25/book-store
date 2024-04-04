from django.db import models
from django.shortcuts import  reverse

# Create your models here.

class Book (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='books/images', null=True, blank=True )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.name
    

    @property
    def show_url(self):
        pass
        url = reverse('books.show_index', args=[self.id])
        return url

    @property    
    def update_url(self):
         pass
         url = reverse('books.update', args=[self.id])
         return url
     
    @property    
    def delete_url(self):
         pass
         url = reverse('books.delete', args=[self.id])
         return url

    
    @property
    def image_url(self):
       return f"/media/{self.image}"    
    