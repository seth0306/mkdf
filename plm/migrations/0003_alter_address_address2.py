# Generated by Django 4.2.3 on 2023-11-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plm', '0002_alter_address_address2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
