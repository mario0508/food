# Generated by Django 3.0.2 on 2020-02-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dilivery', '0002_orderlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlog',
            name='qty',
            field=models.CharField(default='0', max_length=10000),
        ),
    ]
