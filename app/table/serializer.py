from rest_framework import serializers

from .models import Plan, TimeTable


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeTable
        fields = '__all__'
