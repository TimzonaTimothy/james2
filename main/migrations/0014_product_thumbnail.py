# Generated by Django 3.2 on 2022-10-14 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='photos'),
        ),
    ]
