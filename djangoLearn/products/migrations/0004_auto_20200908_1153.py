# Generated by Django 3.1.1 on 2020-09-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200908_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.TextField(),
        ),
    ]