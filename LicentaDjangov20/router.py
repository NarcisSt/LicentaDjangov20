from licentaAPI.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('player', PlayerViewset, basename='player-crud')
router.register('team', TeamViewset, basename='team-crud')
router.register('first-query', FirstQueryViewSet, basename='first-query')
router.register('second-query', SecondQueryViewSet, basename='second-query')
router.register('third-query', ThirdQueryViewSet, basename='third-query')
