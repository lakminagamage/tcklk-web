# Generated by Django 3.0.7 on 2021-09-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210416_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientlogoItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=70)),
                ('image', models.ImageField(default='Defclilog.jpg', upload_to='clientlogo/')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=20)),
                ('image', models.ImageField(default='Defportf.jpg', upload_to='portfolio/')),
                ('sort_by', models.CharField(default='Solutions', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestimonialItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='Deftesti.jpg', upload_to='testimonials/')),
                ('business_name', models.CharField(max_length=200)),
                ('message', models.CharField(default='', max_length=500)),
                ('contact_number', models.CharField(blank=True, max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
