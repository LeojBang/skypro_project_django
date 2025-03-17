from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        context["latest_products"] = Product.objects.all().order_by("-created_at")[:5]
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        if name and phone and message:
            Contact.objects.create(name=name, phone=phone, message=message)

        return redirect("catalog:contacts")
