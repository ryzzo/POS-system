from django.urls import path
from . import views

app_name = 'inventory_management'

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductDetail.as_view()),
    path('categories/', views.CategoryListView.as_view(), name='category-list')
]