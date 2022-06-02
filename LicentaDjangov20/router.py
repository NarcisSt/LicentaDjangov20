from licentaAPI.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('player', PlayerViewset)
router.register('team', TeamViewset)
router.register('first-query', FirstQueryViewSet)
router.register('second-query', SecondQueryViewSet)
router.register('third-query', ThirdQueryViewSet, basename='third-query')
