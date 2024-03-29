# Generated by Django 3.1.4 on 2021-06-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0009_auto_20210613_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlistingsmodel',
            name='CarMakers',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carlistingsmodel',
            name='CarModels',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carlistingsmodel',
            name='CarTrims',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carlistingsmodel',
            name='CarYears',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]
