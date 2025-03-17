import re

from .models import Product
from django.forms import ModelForm
from django.core.exceptions import ValidationError

bad_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "description", "price", "image"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control"})

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in bad_words):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if any(word in description.lower() for word in bad_words):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Неверная цена")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            if image.size > 5 * 1024 * 1025:
                raise ValidationError("Файл больше 5МБ")
            if not (
                image.name.endswith(".jpg")
                or image.name.endswith(".jpeg")
                or image.name.endswith(".png")
            ):
                raise ValidationError("Файл недопустимого формата")
        return image
