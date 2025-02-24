from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    latest_products = Product.objects.all().order_by("-created_at")[:5]

    # Выводим в консоль
    for product in latest_products:
        print(f"Последний продукт: {product.name}, создан: {product.created_at}")

    return render(request, "home.html")


def contacts(request):
    contacts_data = Contact.objects.all()
    latest_products = Product.objects.all().order_by("-created_at")[:5]

    if request.method == "POST":
        name = request.POST.get("name")
        telephone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо {name} за отзыв! Ваше сообщение получено")

    return render(
        request,
        "contacts.html",
        {"contacts": contacts_data, "latest_products": latest_products},
    )
