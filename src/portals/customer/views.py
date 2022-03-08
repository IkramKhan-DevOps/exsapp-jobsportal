from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'


class JobListView(TemplateView):
    template_name = 'customer/jobs_list.html'


class JobDetailView(TemplateView):
    template_name = 'customer/jobs_detail.html'
