# Generated by Django 3.2 on 2022-10-14 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_product_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail2',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
    ]
