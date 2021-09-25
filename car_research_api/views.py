from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework import viewsets
from rest_framework import permissions
from django.core.mail import send_mail
from rest_framework import serializers, status, views
from rest_framework import generics
from rest_framework.response import Response
import os
import re

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
        BodyType = self.request.query_params.get('BodyType', None)
        car_size = self.request.query_params.get('car_size', None)
        car_pricing_tier = self.request.query_params.get('car_pricing_tier', None)
        radius = self.request.query_params.get('radius', 50)
        DriveTrain = self.request.query_params.get('DriveTrain', None)
        starting_price = self.request.query_params.get('starting_price', None)
        ending_price = self.request.query_params.get('ending_price', None)
        starting_mileage = self.request.query_params.get('starting_mileage', None)
        ending_mileage = self.request.query_params.get('ending_mileage', None)
        listingId = self.request.query_params.get('listingId', None)

        car_make_list = []
        car_condition_list = []
        car_model_list = []
        car_trim_list = []
        body_type_list = []

        in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(user_location, radius)]

        if listingId:
            listingIds = listingId.split(',')
            queryset = queryset.filter(ListingId__in = listingIds)
        if car_make:
            car_make_list = car_make.split(',')
            queryset = queryset.filter(CarMakers__in = car_make_list)
        if car_year_start:
            queryset = queryset.filter(CarYears__gte = car_year_start)
        if car_year_end:
            queryset = queryset.filter(CarYears__lte = car_year_end)
        if starting_mileage:
            queryset = queryset.filter(Odometer__gte = starting_mileage)
        if ending_mileage:
            queryset = queryset.filter(Odometer__lte = ending_mileage)
        if car_model:
            car_model_list = car_model.split(',')
            queryset = queryset.filter(CarModels__in = car_model_list)
        if car_trim:
            car_trim_list = car_trim.split(',')
            queryset = queryset.filter(CarTrims__in = car_trim_list)
        if car_year:
            queryset = queryset.filter(CarYears = car_year)
        if BodyType:
            body_type_list = BodyType.split(',')
            queryset = queryset.filter(BodyStyle__in = body_type_list)
        if in_radius:
            queryset = queryset.filter(ZipCode__in = in_radius)
        if starting_price:
            queryset = queryset.filter(Price__gte = starting_price)
        if ending_price:
            queryset = queryset.filter(Price__lte = ending_price)
        if DriveTrain:
            queryset = queryset.filter(DriveTrain = DriveTrain)
        if Condition:
            car_condition_list = Condition.split(',')
            queryset = queryset.filter(Condition__in = car_condition_list)

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

class CarModelsListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows car specs to be viewed or edited.
    """
    serializer_class = CarModelsListingsSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = CarModelsListings.objects.all()
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

class ListingInquiryView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        email_address = request.query_params.get('email_address', None)
        phone_number = request.query_params.get('phone_number', None)
        inquiry_name = request.query_params.get('inquiry_name', None)
        message_body = request.query_params.get('message_body', None)
        if re.fullmatch(regex, email_address):
            send_mail(
                subject = 'Sent email from {}'.format(inquiry_name),
                message = 'Here is the message. {}'.format(message_body),
                from_email = 'jianchtest@gmail.com',
                recipient_list = [email_address],
                fail_silently=False,
            )
            return Response({"success": "Sent"})
        else:
            return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)

        
