# Generated by Django 4.2.3 on 2023-07-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="produit",
            fields=[
                ("id", models.CharField(primary_key=True, serialize=False)),
                ("categories", models.TextField(max_length=5000)),
                ("brands", models.TextField(null=True)),
                ("nutriscore_score", models.IntegerField(null=True)),
                ("quantity", models.TextField(max_length=5000, null=True)),
                ("nutriscore_grade", models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
