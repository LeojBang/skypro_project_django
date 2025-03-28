# Generated by Django 5.1.6 on 2025-03-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                (
                    "preview_image",
                    models.ImageField(upload_to="blog_posts/preview_images"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("publication_sign", models.BooleanField(default=False)),
                ("count_views", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Блог пост",
                "verbose_name_plural": "Блог посты",
                "ordering": ["-created_at"],
            },
        ),
    ]
