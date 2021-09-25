from django.urls import path

from . import views

urlpatterns = [
    path('api/public', views.public),
    path('api/private', views.private),
    path('api/private-scoped', views.private_scoped),
    path('api/user', views.UserAPI.as_view()),
    path('api/plan', views.plan),
    path('api/timetable', views.time_table),
]
