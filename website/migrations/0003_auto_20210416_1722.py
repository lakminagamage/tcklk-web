# Generated by Django 3.0.7 on 2021-04-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contactformmodel_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
