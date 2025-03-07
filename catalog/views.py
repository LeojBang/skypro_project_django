from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


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


class AddProductView(TemplateView):
    template_name = "catalog/add_product.html"
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("catalog:product_list")
        else:
            print(form.errors)  # Выведет ошибки формы в консоль
        return render(request, "add_product.html", {"form": form})
