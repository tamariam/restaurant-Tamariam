# Generated by Django 4.2.8 on 2024-01-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[(0, 'Starter'), (1, 'Main'), (2, 'Dessert')], default='Main', max_length=10),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.CharField(choices=[(0, 'Draft'), (1, 'Published')], default='Draft', max_length=10),
        ),
    ]
