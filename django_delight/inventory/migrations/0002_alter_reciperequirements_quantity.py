# Generated by Django 5.1.7 on 2025-03-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirements',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
