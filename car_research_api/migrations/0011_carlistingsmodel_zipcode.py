# Generated by Django 3.1.4 on 2021-06-27 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0010_auto_20210627_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlistingsmodel',
            name='ZipCode',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
    ]