# Generated by Django 4.0.6 on 2022-08-15 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cordarapp', '0002_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
