# Generated by Django 4.0.3 on 2022-03-29 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_farmacias_hospitales_medicamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentos',
            name='codigo',
            field=models.CharField(max_length=20),
        ),
    ]
