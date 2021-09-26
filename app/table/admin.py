from django.contrib import admin

from .models import User, Plan, TimeTable


@admin.register(User)
class User(admin.ModelAdmin):
    pass


@admin.register(Plan)
class Plan(admin.ModelAdmin):
    pass


@admin.register(TimeTable)
class TimeTable(admin.ModelAdmin):
    pass
