from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Plan, TimeTable
from .serializer import PlanSerializer, TimeTableSerializer


class PlanViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class TimeTableViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
