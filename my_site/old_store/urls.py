from django.contrib import admin
from django.urls import path, include
from .views import (
    ShopIndexView,
    ProductDetailsView,
    ProductsListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    OrderListView,
    OrderDetailView,
    ProductDataExportView,
)

app_name = 'old_store'


urlpatterns = [
    path("", ShopIndexView.as_view(), name='index'),
    path("orders/", OrderListView.as_view(), name='order_list'),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name='order_details'),
    # path("groups/", GroupListView.as_view(), name='groups_list'),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name='products_details'),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name='product_update'),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name='product_delete'),
    path("products/create/", ProductCreateView.as_view(), name='product_create'),
    path("products/", ProductsListView.as_view(), name='product_list'),
    path("products/export/", ProductDataExportView.as_view(), name='product_export'),
]

