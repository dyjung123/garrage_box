from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('delete/<post_id>/', views.delete_post, name='delete_post'),
]
