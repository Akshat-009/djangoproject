from django.contrib import admin
from django.urls import path,include
from home import views



urlpatterns = [
    path('',views.index,name='homepage'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('tracker',views.tracker,name='track'),
    path('search',views.search,name='search'),
    path('product/<int:id>',views.pview,name='pview'),
    path('checkout',views.checkout,name='checkout'),
    path('tracker',views.tracker,name='tracker')
]