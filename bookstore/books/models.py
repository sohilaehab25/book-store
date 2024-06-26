from django.db import models
from django.shortcuts import reverse
from category.models import Category


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    author= models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tag =  models.ForeignKey(Tag,on_delete=models.CASCADE, null=True, blank=True)
    featured = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    @property
    def show_url(self):
        return reverse('books.show_index', args=[self.id])

    @property    
    def update_url(self):
        return reverse('books.update', args=[self.id])
     
    @property    
    def delete_url(self):
        return reverse('books.delete', args=[self.id])

    @property
    def image_url(self):
        return f"/media/{self.image}" 
    
    
       
