# Generated by Django 4.2.8 on 2024-01-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_menu_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='avability',
            new_name='availability',
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('mtarter', 'starter'), ('main', 'main'), ('dessert', 'dessert')], default='Main', max_length=20),
        ),
    ]