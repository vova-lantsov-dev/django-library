# Generated by Django 3.1.7 on 2021-03-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='test/image', upload_to='', verbose_name='Обложка книги'),
            preserve_default=False,
        ),
    ]