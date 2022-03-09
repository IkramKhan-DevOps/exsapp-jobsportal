from django.shortcuts import redirect
from django.views import View
from django.views.generic import (
    TemplateView, CreateView, DetailView, ListView,
    UpdateView, DeleteView)

from src.portals.company.models import Candidate, Job


class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'


class CandidateListView(ListView):
    template_name = 'customer/jobs_list.html'

    def get_queryset(self):
        return Candidate.objects.filter(user=self.request.user)


class CandidateCreateView(CreateView):
    template_name = 'customer/candidate_form.html'
    model = Candidate
    fields = ['__all__']
    success_url = ''


class CandidateUpdateView(UpdateView):
    template_name = 'customer/candidate_form.html'
    model = Candidate
    fields = ['__all__']
    success_url = ''


class CandidateDeleteView(DeleteView):
    template_name = 'customer/candidate_confirm_delete.html'
    model = Candidate
    success_url = ''
