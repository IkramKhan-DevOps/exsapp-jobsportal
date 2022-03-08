from django.urls import path
from .views import (
    DashboardView, JobDetailView, JobListView
)

app_name = 'customer'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('job/', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
]
