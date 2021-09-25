"""cargradient_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from car_research_api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'car-specs',views.CarSpecsViewSet,'carspecs')
router.register(r'car-makers',views.CarMakersViewSet,'carmakers')
router.register(r'car-listings',views.CarListingsViewSet,'carlistings')
router.register(r'car-models',views.CarModelsViewSet,'carmodels')
router.register(r'car-years',views.CarYearsViewSet,'caryears')
router.register(r'car-trims',views.CarTrimsViewSet,'cartrims')
router.register(r'car-listing-models',views.CarModelsListingViewSet,'carlistingmodels')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ListingInquiry/', views.ListingInquiryView.as_view(), name="ListingInquiry"),
]
