# Generated by Django 3.1.4 on 2021-06-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0007_auto_20210613_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='BodySeating',
            field=models.CharField(default='', max_length=54),
        ),
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='DriveTrain',
            field=models.CharField(default='', max_length=56),
        ),
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='Engine',
            field=models.CharField(default='', max_length=57),
        ),
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='ExteriorColor',
            field=models.CharField(default='', max_length=52),
        ),
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='FuelEconomy',
            field=models.CharField(default='', max_length=51),
        ),
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='InteriorColor',
            field=models.CharField(default='', max_length=53),
        ),
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='Transmission',
            field=models.CharField(default='', max_length=55),
        ),
    ]