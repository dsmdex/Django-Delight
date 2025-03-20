# Generated by Django 5.1.7 on 2025-03-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_ingredient_custom_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, choices=[('grams', 'g'), ('pounds', 'lbs'), ('cup', 'c'), ('kilogram', 'kg'), ('tablespoon', 'tbsp'), ('teaspoon', 'tsp'), ('millimeter', 'ml'), ('ounces', 'oz'), ('other', '-')], max_length=10, null=True),
        ),
    ]
