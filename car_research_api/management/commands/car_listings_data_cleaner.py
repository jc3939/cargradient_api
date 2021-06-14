import pymongo
import pandas as pd
from car_research_api.models import CarSpecsModel, CarListingsModel
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    help = 'load car listings data from lake to db.'

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["car_buying"]

    mycol = mydb["car_listings"]

    car_listings_df = pd.DataFrame.from_records(mycol.find())
    @staticmethod
    def create_and_mapping_features(row):
        row['Title'] = row['title']
        row['Odometer'] = '0' if 'Odometer' not in row else row['Odometer']
        row['FuelEconomy'] = row['Fuel Economy']
        row['ExteriorColor'] = row['Exterior Color']
        row['InteriorColor'] = row['Interior Color']
        try:
            row['BodySeating'] = row['Body/Seating']
        except TypeError:
            row['BodySeating'] = row['Body']
        row['DriveTrain'] = row['Drivetrain']
        row['HighlightedFeatures'] = row['highlighted_features']
        row['DetailedSpecs'] = row['detailed_specifications']
        row['Price'] = row['price'] if row['price'] != '' else row['MSRP']
        row['Condition'] = row['condition']
        row['DealerName'] = row['Dealer']
        return row

    def handle(self, *args, **options):
        car_listings_df = self.car_listings_df.apply(self.create_and_mapping_features, axis=1).drop(['_id','title','Fuel Economy', 'Exterior Color','Interior Color','Body/Seating','Drivetrain','highlighted_features','detailed_specifications','MSRP','price','condition','Dealer','Body'],axis=1).to_dict('records')

        size_of_data = len(car_listings_df)
        k = 10
        i = 0
        while i < k:
            print('saving iter: %s' % i)
            model_instances = [CarListingsModel(**item) for item in car_listings_df[i*int(size_of_data/k):(i+1)*int(size_of_data/k)] ]
            CarListingsModel.objects.bulk_create(model_instances)
            i+=1

        model_instances = [CarListingsModel(**item) for item in car_listings_df[i*int(size_of_data/k):] ]
        CarListingsModel.objects.bulk_create(model_instances)
        self.stdout.write(self.style.SUCCESS('Successfully write car listings.'))