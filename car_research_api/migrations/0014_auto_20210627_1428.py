# Generated by Django 3.1.4 on 2021-06-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0013_auto_20210627_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlistingsmodel',
            name='BodyStyle',
            field=models.CharField(default='', max_length=25),
        ),
    ]