from django import forms
from books.models import Book

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'price', 'image', 'category']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        category = cleaned_data.get('category')

        if len(name) < 3:
            self.add_error('name', 'Name must be at least 3 characters long.')

        if price is None :
            self.add_error('plz enter price')

        if category is None:
            self.add_error('category', 'Please select a category.')

        return cleaned_data
