from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.admindashboard, name='admindashboard'),
    path('database/', views.database, name='database'),
    path('delete_item/<int:pk>/', views.deleteData, name='delete_item')
]
