from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='ms18-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('about/', views.about, name='ms18-about'),
]
