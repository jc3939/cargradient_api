# Generated by Django 3.1.4 on 2021-06-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0017_auto_20210627_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModelsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CarModels', models.CharField(default='', max_length=50)),
            ],
        ),
    ]