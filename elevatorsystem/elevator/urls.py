from django.urls import include, path
from rest_framework import routers
from .views import ElevatorViewSet, ElevatorSystemIn,RequestViewSet

router = routers.DefaultRouter()
router.register(r'elevators', ElevatorViewSet,basename="elevator")
router.register(r'floors', RequestViewSet,basename="request")
router.register(r'elevatorsystem', ElevatorSystemIn,basename="elevatorsystem")

urlpatterns = [
    path('', include(router.urls)),
]