from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
        path('index/', views.index, name='index'),
        path('book/<int:book_id>', views.detail, name='detail'),
        path('add_book/', views.add_book , name='add_book'),
        path('update/<int:id>', views.update, name='update'),
        path('delete/<int:id>', views.delete, name='delete'),
] 