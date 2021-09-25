from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, Plan, TimeTable

admin.site.register(User, UserAdmin)
admin.site.register(Plan)
admin.site.register(TimeTable)
