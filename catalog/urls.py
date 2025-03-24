from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/product_detail/<int:pk>",
        ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "products/update_product/<int:pk>",
        ProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "products/delete_product/<int:pk>",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
