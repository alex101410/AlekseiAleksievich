# Generated by Django 4.0.6 on 2022-07-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparser', '0002_alter_product_options_alter_product_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='article',
            field=models.TextField(unique=True, verbose_name='Артикл'),
        ),
    ]
