from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """ Получает данные по продуктам из кеша, если кеш пустой, то получает из БД """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)

    if products is not None:
        return products

    products = Product.objects.all()
    cache.set(key, products)

    return products

class ProductService:

    @staticmethod
    def get_products_from_category(category_id):
        products = Product.objects.filter(category=Category.objects.get(pk=category_id))
        return products