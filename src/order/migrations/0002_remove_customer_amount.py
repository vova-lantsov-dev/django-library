# Generated by Django 3.1.7 on 2021-03-27 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='amount',
        ),
    ]
