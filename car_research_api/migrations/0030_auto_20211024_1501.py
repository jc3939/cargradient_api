# Generated by Django 3.1.4 on 2021-10-24 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0029_auto_20211024_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspecsmodel',
            name='BasicSpec_Trim',
            field=models.CharField(default='', max_length=200),
        ),
    ]
