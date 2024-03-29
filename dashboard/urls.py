from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('banner-list/', views.list_banner, name='list_banner'),
    path('banner-create/', views.create_banner, name='create_banner'),
    path('banner-detail/<int:id>/', views.banner_detail, name='banner_detail'),
    path('banner-edit/<int:id>/', views.banner_edit, name='banner_edit'),
    path('banner-delete/<int:id>/', views.banner_delete, name='banner_delete'),
    
    path('service-list/', views.list_service, name='list_service'),
    path('service-create/', views.create_service, name='create_service'),
    path('service-detail/<int:id>/', views.service_detail, name='service_detail'),
    path('service-edit/<int:id>/', views.service_edit, name='service_edit'),
    path('service-delete/<int:id>/', views.service_delete, name='service_delete'),

    path('aboutus-list/', views.list_aboutus, name='list_aboutus'),
    path('aboutus-create/', views.create_aboutus, name='create_aboutus'),
    path('aboutus-detail/<int:id>/', views.aboutus_detail, name='aboutus_detail'),
    path('aboutus-edit/<int:id>/', views.aboutus_edit, name='aboutus_edit'),
    path('aboutus-delete/<int:id>/', views.aboutus_delete, name='aboutus_delete'),

    path('price-list/', views.list_price, name='list_price'),
    path('price-create/', views.create_price, name='create_price'),
    path('price-detail/<int:id>/', views.price_detail, name='price_detail'),
    path('price-edit/<int:id>/', views.price_edit, name='price_edit'),
    path('price-delete/<int:id>/', views.price_delete, name='price_delete'),

    path('contact-list/', views.list_contact, name='list_contact'),
    path('contact-detail/<int:id>/', views.contact_detail, name='contact_detail'),
    path('contact-edit/<int:id>/', views.contact_edit, name='contact_edit'),
    path('contact-delete/<int:id>/', views.contact_delete, name='contact_delete'),
]