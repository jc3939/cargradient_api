# Generated by Django 3.1.4 on 2021-09-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_research_api', '0026_auto_20210921_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingInquiryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('inquiry_name', models.CharField(default='', max_length=50)),
                ('message_body', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
