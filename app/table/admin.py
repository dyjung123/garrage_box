from django.contrib import admin

from .models import User, Plan, TimeTable


@admin.register(User)
class User(admin.ModelAdmin):
  pass


@admin.register(Plan)
class Entry(admin.ModelAdmin):
  pass


@admin.register(TimeTable)
class Entry(admin.ModelAdmin):
  pass
