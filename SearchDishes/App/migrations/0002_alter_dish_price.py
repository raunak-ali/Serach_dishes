# Generated by Django 4.2.3 on 2023-07-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.TextField(blank=True, null=True),
        ),
    ]
