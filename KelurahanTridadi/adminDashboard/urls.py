from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.admindashboard, name='admindashboard'),
    path('database/', views.database, name='database'),
    path('data_form/', views.dataform, name='data_form'),
    path('update_data/<int:pk>/', views.updatedata, name='update_data'),
    path('penanganan/<int:pk>/', views.penanganandata, name='penanganan'),
    path('delete_item/<int:pk>/', views.deleteData, name='delete_item'),
    path('vaksinasi/', views.dataVaksinasi, name='vaksinasi'),
    path('vaksinasi_form/', views.vaksinasiform, name='vaksinasi_form'),
    path('delete_vaksinasi/<int:pk>', views.deleteVaksin, name='delete_vaksinasi'),
    path('update_vaksinasi/<int:pk>/', views.updateVaksinasi, name='update_vaksinasi'),
]
