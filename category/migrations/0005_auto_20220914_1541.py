# Generated by Django 3.0.1 on 2022-09-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20220914_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
