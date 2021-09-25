from rest_framework import serializers
from .models import User, Plan, TimeTable


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Plan
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    # plan = PlanSerializer()

    class Meta:
        model = TimeTable
        fields = '__all__'

