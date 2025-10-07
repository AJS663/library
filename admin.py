from django.contrib import admin
from .models import book, borrowRecord

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'isbn', 'available')
    search_fields=('title', 'author', 'isbn', 'available')
    list_filter=('title', 'author')

admin.site.register(book, BookAdmin)

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display=('book', 'user', 'loan_date', 'return_date')
    search_fields=('book', 'user', 'loan_date', 'return_date')
    list_filter=('book', 'user')
    
admin.site.register(borrowRecord, BorrowRecordAdmin)
