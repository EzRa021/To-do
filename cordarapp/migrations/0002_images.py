# Generated by Django 4.0.6 on 2022-08-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cordarapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
