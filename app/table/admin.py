from django.contrib import admin

from .models import Plan, TimeTable


@admin.register(Plan)
class Plan(admin.ModelAdmin):
    pass


@admin.register(TimeTable)
class TimeTable(admin.ModelAdmin):
    pass
