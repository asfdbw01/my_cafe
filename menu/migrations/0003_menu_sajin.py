# Generated by Django 4.2.5 on 2023-10-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='sajin',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]