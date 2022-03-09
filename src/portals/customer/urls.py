from django.urls import path
from .views import (
    DashboardView, CandidateListView, CandidateCreateView, CandidateDeleteView, CandidateUpdateView
)

app_name = 'customer'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    path('job/', DashboardView.as_view(), name='application-list'),
    path('job/<int:pk>/apply/', DashboardView.as_view(), name='application-apply'),
    path('job/application/<int:pk>/update/', DashboardView.as_view(), name='application-update'),
    path('job/application/<int:pk>/delete/', DashboardView.as_view(), name='application-delete'),
]
