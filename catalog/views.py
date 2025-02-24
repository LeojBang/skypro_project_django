from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Contact


def home(request):
    products_list = Product.objects.all()
    context = {"products_list": products_list}
    return render(request, "home.html", context)


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_info.html", context)


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
