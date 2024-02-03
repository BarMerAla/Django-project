from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('item/<int:item_id>/', views.detail, name = 'detail'),
    path('add/', views.add_product, name='add'),
    path('delete/', views.delete_product, name='delete'),
    path('search/', views.search, name='search'),
    path('category/', views.category, name='category'),
    path("contact", views.contact, name="contact"),
]

