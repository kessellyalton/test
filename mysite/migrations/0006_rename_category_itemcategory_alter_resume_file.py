# Generated by Django 5.1.3 on 2024-11-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0005_businesscategory_business"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Category",
            new_name="ItemCategory",
        ),
        migrations.AlterField(
            model_name="resume",
            name="file",
            field=models.FileField(upload_to="resume/"),
        ),
    ]
