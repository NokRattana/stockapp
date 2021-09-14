from django.urls import path
from . import views



urlpatterns = [
    path('', views.stocks_temp, name='stocks_temp'),
    path('blog_temp.html', views.about_temp, name='blog_temp'),
    path('add_mystock.html', views.add_mystock, name="add_mystock"),
    
]

