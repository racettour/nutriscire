# Generated by Django 4.2.3 on 2023-07-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0007_alter_produit_brands"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produit", name="brands", field=models.TextField(null=True),
        ),
    ]
