from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, TemplateView

from src.portals.company.bll import get_user_company_bll
from .models import Job, Category, Company


class DashboardView(TemplateView):
    template_name = 'company/dashboard.html'


class CompanyUpdateView(UpdateView):
    model = Company
    fields = [
        'name', 'tag_line', 'description',
        'business_type', 'contact_number',
        'contact_email', 'contact_address'
    ]

    def get_object(self, queryset=None):
        return get_user_company_bll(self.request.user)


class JobListView(ListView):
    model = Job

    def get_queryset(self):
        return Job.objects.filter(company__user=self.request.user)


class JobCreateView(CreateView):
    model = Job
    fields = ['title', 'category', 'description']
    success_url = ''

    def form_valid(self, form):
        form.instance.company = get_user_company_bll(self.request.user)
        return super(JobCreateView, self).form_valid(form)


class JobUpdateView(UpdateView):
    model = Job
    fields = ['title', 'category', 'description', 'status']
    success_url = ''

    def get_object(self, queryset=None):
        return get_object_or_404(
            Job.objects.filter(
                company__user=self.request.user
            ), pk=self.kwargs['pk']
        )


class JobDeleteView(DeleteView):
    model = Job
    success_url = ''

    def get_object(self, queryset=None):
        return get_object_or_404(
            Job.objects.filter(
                company__user=self.request.user
            ), pk=self.kwargs['pk']
        )

