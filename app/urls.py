from django.contrib import admin
from django.urls import path
from . import views
#Create Path for html files to render from one page to another page

urlpatterns = [
    
    path('',views.home, name='home'),
    path('contact-detail/<int:id>/',views.contact_detail,name = 'contact-detail'),
    path('add-contact/',views.add_contact, name='add-contact'),
    path('edit-contact/<int:id>/', views.edit_contact, name= 'edit-contact'),
    path('delete-contact/<int:id>/', views.delete_contact, name= 'delete-contact'),
]
