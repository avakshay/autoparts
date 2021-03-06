# Generated by Django 3.1.7 on 2021-05-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, default='img', upload_to='productimg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, default='img', upload_to='productimg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, default='img', upload_to='productimg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image4',
            field=models.ImageField(blank=True, default='img', upload_to='productimg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.FloatField(blank=True),
        ),
    ]
