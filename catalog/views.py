from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
    UpdateView,
)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        """Возвращает форму в зависимости от прав пользователя."""
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied

    def get_queryset(self):
        """Ограничиваем доступ только к своим товарам или для модераторов."""
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return Product.objects.all()
        return Product.objects.filter(owner=self.request.user)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_queryset(self):
        """Ограничиваем доступ к удалению только владельцу или модератору."""
        if self.request.user.has_perm("catalog.delete_product"):
            return Product.objects.all()
        return Product.objects.filter(owner=self.request.user)


class ContactsView(LoginRequiredMixin, TemplateView):
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
