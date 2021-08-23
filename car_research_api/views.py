from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework import viewsets
from rest_framework import permissions
from pyzipcode import ZipCodeDatabase

from car_research_api.serializers import *
from car_research_api.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    User = get_user_model()
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarSpecsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarSpecsSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = CarSpecsModel.objects.all()
        car_make = self.request.query_params.get('car_make', None)
        car_model = self.request.query_params.get('car_model', None)
        car_trim = self.request.query_params.get('car_trim', None)
        car_year = self.request.query_params.get('car_year', None)
        if car_make is not None:
            queryset = queryset.filter(BasicSpec_Make = car_make)
        if car_model is not None:
            queryset = queryset.filter(BasicSpec_Model = car_model)
        if car_trim is not None:
            queryset = queryset.filter(BasicSpec_Trim = car_trim)
        if car_year is not None:
            queryset = queryset.filter(BasicSpec_Year = car_year)
        return queryset

class CarMakersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarMakersSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = CarMakersModel.objects.all()
        car_make = self.request.query_params.get('car_make', None)
        if car_make is not None:
            queryset = queryset.filter(BasicSpec_Make = car_make)
        return queryset

class CarListingsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarListingsSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        zcdb = ZipCodeDatabase()
        queryset = CarListingsModel.objects.all()
        Condition = self.request.query_params.get('Condition', None)
        car_make = self.request.query_params.get('CarMakers', None)
        car_model = self.request.query_params.get('CarModels', None)
        car_trim = self.request.query_params.get('CarTrims', None)
        car_year = self.request.query_params.get('CarYears', None)
        car_year_start = self.request.query_params.get('car_year_start', None)
        car_year_end = self.request.query_params.get('car_year_end', None)
        user_location = self.request.query_params.get('user_location', '98052')
        BodyStyle = self.request.query_params.get('BodyStyle', None)
        car_size = self.request.query_params.get('car_size', None)
        car_pricing_tier = self.request.query_params.get('car_pricing_tier', None)
        radius = self.request.query_params.get('radius', 50)
        DriveTrain = self.request.query_params.get('DriveTrain', None)
        starting_price = self.request.query_params.get('starting_price', None)
        ending_price = self.request.query_params.get('ending_price', None)
        starting_mileage = self.request.query_params.get('starting_mileage', None)
        ending_mileage = self.request.query_params.get('ending_mileage', None)

        in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(user_location, radius)]

        if car_make:
            queryset = queryset.filter(CarMakers = car_make)
        if car_year_start:
            queryset = queryset.filter(CarYears__gte = car_year_start)
        if car_year_end:
            queryset = queryset.filter(CarYears__lte = car_year_end)
        if car_year_end:
            queryset = queryset.filter(Odometer__gte = starting_mileage)
        if ending_mileage:
            queryset = queryset.filter(Odometer__lte = ending_mileage)
        if car_model:
            queryset = queryset.filter(CarModels = car_model)
        if car_trim:
            queryset = queryset.filter(CarTrims = car_trim)
        if car_year:
            queryset = queryset.filter(CarYears = car_year)
        if BodyStyle:
            queryset = queryset.filter(BodyStyle = BodyStyle)
        if in_radius:
            queryset = queryset.filter(ZipCode__in = in_radius)
        if starting_price:
            queryset = queryset.filter(Price__gte = starting_price)
        if ending_price:
            queryset = queryset.filter(Price__lte = ending_price)
        if DriveTrain:
            queryset = queryset.filter(DriveTrain = DriveTrain)
        if Condition:
            queryset = queryset.filter(Condition = Condition)

        return queryset

class CarModelsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarModelsSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = CarModelsModel.objects.all()
        car_maker = self.request.query_params.get('car_make', None)
        if car_maker is not None:
            queryset = queryset.filter(BasicSpec_Make = car_maker)
        return queryset

class CarYearsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarYearsSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = CarYearsModel.objects.all()
        car_make = self.request.query_params.get('car_make', None)
        car_model = self.request.query_params.get('car_model', None)
        if car_make is not None:
            queryset = queryset.filter(BasicSpec_Make = car_make)
        if car_model is not None:
            queryset = queryset.filter(BasicSpec_Model = car_model)
        return queryset

class CarTrimsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarTrimsSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = CarTrimsModel.objects.all()
        car_make = self.request.query_params.get('car_make', None)
        car_model = self.request.query_params.get('car_model', None)
        car_year = self.request.query_params.get('car_year', None)
        if car_make is not None:
            queryset = queryset.filter(BasicSpec_Make = car_make)
        if car_model is not None:
            queryset = queryset.filter(BasicSpec_Model = car_model)
        if car_year is not None:
            queryset = queryset.filter(BasicSpec_Year = car_year)
        return queryset