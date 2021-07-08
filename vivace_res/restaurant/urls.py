from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('home/', views.load_home, name="home"),
    path('home/contact/', views.submit_contact, name='contact'),
    path('home/book/', views.submit_booking, name='book'),
]
