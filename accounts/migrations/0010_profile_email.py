# Generated by Django 3.2.6 on 2021-09-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210601_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
    ]
