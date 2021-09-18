from rest_framework import serializers

from .models import User, Plan, TimeTable


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'uesrname', 'email', 'enabled', 'created_at', 'updated_at')


class PlanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Plan
    fields = ('id', 'user_id', 'title', 'description', 'evaluation', 'start', 'end', 'created_at', 'updated_at')


class TimeTableSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeTable
    fields = ('id', 'plan_id', 'title', 'memo', 'from_at', 'to_at', 'created_at', 'updated_at')