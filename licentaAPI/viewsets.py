from rest_framework import viewsets
from . import models
from . import serializers


class TeamViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        queryset = models.Teams.objects.all()
        query = str(models.Teams.objects.all().explain(verbose=True, analyze=True))
        print(query)
        print("|")
        print("|")
        return queryset


class PlayerViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PlayerSerializer

    def get_queryset(self):
        queryset = models.Players.objects.all()
        query = str(models.Players.objects.all().explain(verbose=True, analyze=True))
        print(query)
        print("|")
        print("|")
        return queryset


class FirstQueryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlayerSerializer

    def get_queryset(self):
        queryset = models.Players.objects.select_related('team').filter(position__contains='CB').filter(
            team__players__position__endswith='United')
        query = str(models.Players.objects.select_related('team').filter(position__contains='CB').filter(
            team__players__position__endswith='United').explain(verbose=True, analyze=True))
        print(query)
        print("|")
        print("|")
        return queryset


class SecondQueryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlayerSerializer

    def get_queryset(self):
        queryset = models.Players.objects.all().order_by("id")
        query = str(models.Players.objects.all().order_by("id").explain(verbose=True, analyze=True))
        print(query)
        print("|")
        print("|")
        return queryset


class ThirdQueryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        queryset = models.Teams.objects.all().filter(points__gt=10)
        query = str(models.Teams.objects.all().filter(points__gt=10).explain(verbose=True, analyze=True))
        print(query)
        print("|")
        print("|")
        return queryset

