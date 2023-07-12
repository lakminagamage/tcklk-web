# Generated by Django 3.1 on 2021-03-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210330_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aboutme',
            field=models.TextField(default='your Bio'),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contactno',
            field=models.TextField(default='+94 712345678'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.TextField(default='Sri Lanka'),
        ),
        migrations.AddField(
            model_name='profile',
            name='postalcode',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='socialcontacts',
            field=models.TextField(blank=True),
        ),
    ]
