from rest_framework import routers
from .views import UserViewSet, PlanViewSet, TimeTableViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'timetables', TimeTableViewSet)
