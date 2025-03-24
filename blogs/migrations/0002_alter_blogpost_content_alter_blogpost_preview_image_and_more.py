# Generated by Django 5.1.6 on 2025-03-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=models.TextField(
                help_text="Введите содержание поста", verbose_name="Содержание поста"
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="preview_image",
            field=models.ImageField(
                upload_to="blog_posts/preview_images",
                verbose_name="Превью изображение поста",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="publication_sign",
            field=models.BooleanField(default=False, verbose_name="Публикация поста"),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(
                help_text="Введите заголовок поста",
                max_length=255,
                verbose_name="Заголовок поста",
            ),
        ),
    ]
