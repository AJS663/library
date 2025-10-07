from django.contrib import admin
from django.urls import include, path

from Libraryapp import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('Libraryapp.urls')), # replace with your app name
]


from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('news/', views.news, name='news'),
path('registration/', views.registration, name="registration"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
]
