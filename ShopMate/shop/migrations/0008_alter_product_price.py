# Generated by Django 4.1.7 on 2023-07-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
