from rest_framework import viewsets
from . import models
from . import serializers
from django.db import connection
from datetime import datetime

class TeamViewset(viewsets.ModelViewSet):
    queryset = models.Teams.objects.all()
    serializer_class = serializers.TeamSerializer


class PlayerViewset(viewsets.ModelViewSet):
    queryset = models.Players.objects.all()
    serializer_class = serializers.PlayerSerializer


class FirstQueryViewSet(viewsets.ModelViewSet):
    queryset = models.Players.objects.select_related('team').filter(position__contains='CB').filter(
        team__players__position__endswith='United')
    serializer_class = serializers.PlayerSerializer


class SecondQueryViewSet(viewsets.ModelViewSet):
    queryset = models.Players.objects.all().order_by("id")
    serializer_class = serializers.PlayerSerializer


class ThirdQueryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        # points = self.kwargs['pk']
        queryset = models.Teams.objects.all().filter(points__gt=10)
        query = str(models.Teams.objects.all().filter(points__gt=10).explain())
        query_with_explain = f'EXPLAIN {query}'
        print(query_with_explain)
        return queryset
