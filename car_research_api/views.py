from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions
from car_research_api.serializers import UserSerializer, CarSpecsSerializer

from car_research_api.models import CarSpecsModel


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

