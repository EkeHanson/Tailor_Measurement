# Generated by Django 5.0 on 2024-01-15 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('phone_number', models.CharField(max_length=15)),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_style', models.CharField(max_length=100)),
                ('round_neck', models.FloatField()),
                ('shoulder', models.FloatField()),
                ('top_length', models.FloatField()),
                ('long_sleeve', models.FloatField()),
                ('short_sleeve', models.FloatField()),
                ('round_sleeve', models.FloatField()),
                ('chest', models.FloatField()),
                ('down_length', models.FloatField()),
                ('knee', models.FloatField()),
                ('round_knee', models.FloatField()),
                ('bottom', models.FloatField()),
                ('hip', models.FloatField()),
                ('waist', models.FloatField()),
                ('thigh', models.FloatField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persons.customer')),
            ],
        ),
    ]
