from django.db import models

# Create your models here.

from django.db import models

class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

def __str__(self): 
        return self.title

class borrowRecord(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

def __str__(self): 
     return f"{self.user} borrowed '{self.book.title}'"






