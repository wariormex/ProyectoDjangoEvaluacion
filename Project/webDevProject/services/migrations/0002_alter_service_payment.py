# Generated by Django 4.1.1 on 2022-11-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='payment',
            field=models.CharField(choices=[('Single Payment', 'Perpetual License'), ('per Month', 'Monthly Subscription'), ('per Year', 'Yearly Subscription')], max_length=200, verbose_name='Contenido'),
        ),
    ]
