# Generated by Django 4.1.1 on 2022-11-05 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_portfolioitem_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitemimage',
            name='portfolioItem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='portfolioitem_images', to='portfolio.portfolioitem'),
        ),
    ]
