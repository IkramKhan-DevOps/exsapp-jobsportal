from django.urls import path
from .views import (
    JobUpdateView, JobListView, JobCreateView, JobDeleteView,
    DashboardView, CompanyUpdateView
)


app_name = 'company'
urlpatterns = [
    path('', CompanyUpdateView.as_view(), 'company-update'),
    path('company/profile/', CompanyUpdateView.as_view(), 'company-update'),
    path('job/', JobListView.as_view(), 'job-list'),
    path('job/add/', JobCreateView.as_view(), 'job-add'),
    path('job/<int:pk>/change/', JobUpdateView.as_view(), 'job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), 'job-delete'),
]
