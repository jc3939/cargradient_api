from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
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
        queryset = CarListingsModel.objects.all()
        condition = self.request.query_params.get('condition', None)
        car_make = self.request.query_params.get('car_make', None)
        car_model = self.request.query_params.get('car_model', None)
        car_trim = self.request.query_params.get('car_trim', None)
        car_year = self.request.query_params.get('car_year', None)
        user_location = self.request.query_params.get('user_location', None)
        body_type = self.request.query_params.get('body_type', None)
        car_size = self.request.query_params.get('car_size', None)
        car_pricing_tier = self.request.query_params.get('car_pricing_tier', None)

        if car_make is not None:
            queryset = queryset.filter(CarMakers = car_make)
        if car_model is not None:
            queryset = queryset.filter(CarModels = car_model)
        if car_trim is not None:
            queryset = queryset.filter(CarTrims = car_trim)
        if car_year is not None:
            queryset = queryset.filter(CarYears = car_year)
        if condition is not None:
            queryset = queryset.filter(Condition = condition)
        if user_location is not None:
            queryset = queryset.filter(ZipCode = user_location)
        if body_type is not None:
            queryset = queryset.filter(BodyStyle = body_type)
        return queryset

class CarModelsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarModelsSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = CarModelsModel.objects.all()
        return queryset