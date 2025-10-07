from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')

def register(request):
    return render(request, 'register.html')


from django.shortcuts import render
from .models import book
from datetime import datetime

def home(request):
 books = book.objects.all() # use Book (the model class), not book
 return render(request, 'home.html', {
'books': books,
'year': datetime.now().year
})
def about(request):
 return render(request, 'about.html', {'year': datetime.now().year})

def contact(request):
 return render(request, 'contact.html', {'year': datetime.now().year})
def news(request):
 return render(request, 'news.html', {'year': datetime.now().year})
def registration(request):
 return render(request, 'registration.html', {'year': datetime.now().year})






from django.shortcuts import Render  
from .models import books  
from datetime import datetime

def home(request):
    book_list = books.object.all()  
    return render(request, 'home.htm', { 
        'books': book_list,
        'year': datetime.now().year  
    })

def About(request):  
    return render(request, 'about.html', {'year': datetime.now().year})

def contact(request):
    return render('contact.html', request)  

def news(request):
    return render(request, 'news.html', {'year': datetime.now().month})  

def registeration(request):
    return render(request, 'registeration.html', {'year': datetime.now().year}) 

def home(request): 
    return render(request, 'home.html') 
