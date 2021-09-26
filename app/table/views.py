from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import User, Plan, TimeTable
from .serializer import UserSerializer, PlanSerializer, TimeTableSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
