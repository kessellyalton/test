# Generated by Django 5.1.3 on 2024-11-07 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0009_teammember"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                ("author_name", models.CharField(max_length=100)),
                ("author_title", models.CharField(max_length=150)),
                ("quote", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="testimonials/"),
                ),
                ("twitter_url", models.URLField(blank=True, null=True)),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("instagram_url", models.URLField(blank=True, null=True)),
                ("linkedin_url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
