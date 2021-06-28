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

        def determine_make_model_trim(source):
            title_splitted = source.split()
            year = title_splitted[1]
            maker = title_splitted[2]
            try:
                model_trim = ' '.join(title_splitted[3:title_splitted.index("For")])
            except ValueError:
                print(source)
                exit()
            if model_trim[0].isdigit():
                model = model_trim[0]+'-series'
                trim = model_trim[1:]
            elif len(model_trim.split()) == 1:
                model = model_trim
                trim = "Base"
            else:
                model = model_trim.split()[0]
                trim = ' '.join(model_trim.split()[1:])
            return year, maker, model, trim

        if 'Odometer' not in row:
            row['Odometer'] = '0'
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
        if row['Price'] == '':
            row['Price'] = row['MSRP']
        row['DealerName'] = row['Dealer']
        row['CarYears'], row['CarMakers'], row['CarModels'], row['CarTrims'] = determine_make_model_trim(row['Title'])
        row['ZipCode'] = "98005"
        try:
            row["BodyStyle"] = row['BodySeating'].split('/')[0]
        except AttributeError:
            row["BodyStyle"] = ""
        return row

    def handle(self, *args, **options):
        car_listings_df = self.car_listings_df.apply(self.create_and_mapping_features, axis=1).drop(['_id','Fuel Economy', 'Exterior Color','Interior Color','Body/Seating','Drivetrain','highlighted_features','detailed_specifications','MSRP','Dealer','Body'],axis=1).to_dict('records')

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