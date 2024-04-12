from django.contrib import admin
from .models import Book

def mark_as_featured(modeladmin, request, queryset):
    selected_books_count = queryset.count()
    if selected_books_count > 5:
        modeladmin.message_user(request, "You can only select up to 5 books as featured.", level='ERROR')
    else:
        queryset.update(featured=True)

mark_as_featured.short_description = "Mark selected books as featured (max 5)"

class BookAdmin(admin.ModelAdmin):
    list_display = ['price','name','featured']
    list_editable = ['featured']
    list_display_links = None
    actions = [mark_as_featured]

admin.site.register(Book, BookAdmin)
