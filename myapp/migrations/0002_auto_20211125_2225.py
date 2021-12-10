# Generated by Django 3.2.9 on 2021-11-26 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=50)),
                ('passport_number', models.CharField(max_length=30)),
                ('dept_airport', models.CharField(max_length=50)),
                ('arrive_airport', models.CharField(max_length=30)),
                ('flight_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]