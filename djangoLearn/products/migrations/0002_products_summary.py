# Generated by Django 3.1.1 on 2020-09-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='summary',
            field=models.TextField(default='This is cool!'),
        ),
    ]