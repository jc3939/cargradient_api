# Generated by Django 3.1.4 on 2021-06-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0016_auto_20210627_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='CarYears',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='ZipCode',
            field=models.CharField(max_length=50),
        ),
    ]
