# Generated by Django 3.2.9 on 2021-11-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_passenger_url_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='url_image',
            field=models.CharField(default='', max_length=255),
        ),
    ]