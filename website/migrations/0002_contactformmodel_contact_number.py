# Generated by Django 3.0.7 on 2021-04-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactformmodel',
            name='contact_number',
            field=models.CharField(default='', max_length=13),
        ),
    ]