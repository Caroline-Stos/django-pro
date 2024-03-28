from django.urls import path
from django.contrib import admin
from mycontacts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.show, name='show'),
    path("add/", views.add, name='add'),
    path('contact/<int:contact_id>/', views.view_contact, name='view_contact'),
    path('edit/<int:contact_id>/', views.edit_contact, name='edit')
] 