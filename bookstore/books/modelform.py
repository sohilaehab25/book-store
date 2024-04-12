from django import forms
from books.models import Book
# from books.models import Tag
from .models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name'] 

class BookModelForm(forms.ModelForm):
    # tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Book
        fields = ['name', 'price', 'image', 'category','tag', 'author']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        category = cleaned_data.get('category')
        tag= cleaned_data.get('tag')
        author = cleaned_data.get('author')

        if len(name) < 3:
            self.add_error('name', 'Name must be at least 3 characters long.')

        if price is None :
            self.add_error('plz enter price')

        if category is None:
            self.add_error('category', 'Please select a category.')

        if tag is None:
            self.add_error('tag', 'Please select a tag.')
        if author is None:
            self.add_error('author', 'Please enter author.')

        return cleaned_data
