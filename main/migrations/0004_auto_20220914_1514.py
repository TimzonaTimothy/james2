# Generated by Django 3.0.1 on 2022-09-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220914_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='score',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
