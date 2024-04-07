from django.db import models
from django.shortcuts import  get_object_or_404, reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def get_all_categories(cls):
        categories = cls.objects.all()
        return categories
    
    @classmethod
    def get_category_byid(cls,id):
        return get_object_or_404(cls,pk=id)
    
    @property
    def logo_url(self):
        return f"/media/{self.logo}"
    
    @property
    def show_url(self):
        url= reverse('categories.show', args=[self.id])
        return url
    
    @property    
    def delete_url(self):
         pass
         url = reverse('categories.delete', args=[self.id])
         return url
     
    # @property    
    # def update_url(self):
    #      pass
    #      url = reverse('categories.update', args=[self.id])
    #      return url
     
    @property    
    def create_url(self):
         pass
         url = reverse('categories.index', args=[self.id])
         return url 
 
 

    
    
    
