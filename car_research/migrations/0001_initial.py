# Generated by Django 3.1.4 on 2021-11-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarListingsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ListingId', models.IntegerField(default=0)),
                ('Title', models.CharField(default='', max_length=200)),
                ('Odometer', models.IntegerField(default=0)),
                ('FuelEconomy', models.CharField(default='', max_length=50)),
                ('FuelType', models.CharField(default='', max_length=20)),
                ('ExteriorColor', models.CharField(default='', max_length=50)),
                ('InteriorColor', models.CharField(default='', max_length=50)),
                ('BodySeating', models.CharField(default='', max_length=50)),
                ('Transmission', models.CharField(default='', max_length=50)),
                ('DriveTrain', models.CharField(default='', max_length=100)),
                ('Engine', models.CharField(default='', max_length=50)),
                ('HighlightedFeatures', models.JSONField(null=True)),
                ('DetailedSpecs', models.JSONField(null=True)),
                ('Price', models.IntegerField(default=0)),
                ('Condition', models.CharField(max_length=10)),
                ('DealerName', models.CharField(max_length=20)),
                ('CarMakers', models.CharField(max_length=20)),
                ('CarModels', models.CharField(max_length=20)),
                ('CarTrims', models.CharField(max_length=100)),
                ('CarYears', models.CharField(max_length=50)),
                ('ZipCode', models.CharField(max_length=50)),
                ('BodyStyle', models.CharField(default='', max_length=25)),
                ('ImageUrls', models.JSONField(null=True)),
                ('DetailedAddress', models.CharField(default='', max_length=100)),
                ('City', models.CharField(default='', max_length=20)),
                ('State', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CarMakersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BasicSpec_Make', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarModelsListings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BasicSpec_Year', models.CharField(default='', max_length=50)),
                ('BasicSpec_Make', models.CharField(default='', max_length=50)),
                ('BasicSpec_Model', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarModelsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BasicSpec_Make', models.CharField(default='', max_length=50)),
                ('BasicSpec_Model', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarSpecsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WindowsandMirrors_RearWiper', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarTrimsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BasicSpec_Year', models.CharField(default='', max_length=50)),
                ('BasicSpec_Make', models.CharField(default='', max_length=50)),
                ('BasicSpec_Model', models.CharField(default='', max_length=50)),
                ('BasicSpec_Trim', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarYearsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BasicSpec_Year', models.CharField(default='', max_length=50)),
                ('BasicSpec_Make', models.CharField(default='', max_length=50)),
                ('BasicSpec_Model', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ListingInquiryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('inquiry_name', models.CharField(default='', max_length=50)),
                ('message_body', models.CharField(default='', max_length=500)),
                ('email_subscribed', models.BooleanField(default=False)),
                ('car_listing_url', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
