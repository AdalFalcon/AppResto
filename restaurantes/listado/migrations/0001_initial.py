# Generated by Django 5.1.2 on 2024-11-05 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restataurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_restaurant', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('Razon_social', models.CharField(blank=True, max_length=255, null=True)),
                ('class_activity', models.CharField(max_length=255)),
                ('estratum', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=255)),
                ('num_exterior', models.CharField(blank=True, max_length=255, null=True)),
                ('num_interior', models.CharField(blank=True, max_length=255, null=True)),
                ('colony', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('service_type', models.CharField(max_length=50)),
            ],
        ),
    ]
