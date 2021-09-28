from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'plans', views.PlanViewSet)
router.register(r'timetables', views.TimeTableViewSet)
