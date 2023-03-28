# Generated by Django 4.1.5 on 2023-01-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fines", "0002_alter_inscription_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inscription",
            name="cellphone_2",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="inscription",
            name="dni",
            field=models.IntegerField(unique=True, verbose_name="DNI"),
        ),
    ]
