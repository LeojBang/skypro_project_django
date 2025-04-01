from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView, ProductsByCategoryView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "products/product_detail/<int:pk>",cache_page(60)(ProductDetailView.as_view()),
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
    path("product_category_list/<int:category_id>/", ProductsByCategoryView.as_view(), name="product_category_list"),

    path("contacts/", ContactsView.as_view(), name="contacts"),
]
