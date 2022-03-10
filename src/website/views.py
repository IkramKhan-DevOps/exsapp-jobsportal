from django.core.paginator import Paginator
from django.views.generic import TemplateView, DetailView, ListView

from src.portals.company.filters import JobFilter
from src.portals.company.models import Job


class HomeView(ListView):
    template_name = 'website/home.html'
    paginate_by = 20
    model = Job

    def get_context_data(self, **kwargs):
        jobs_candidate_user = Job.objects.filter(candidate__user=self.request.user).values('pk')
        jobs_liked_by_user = Job.objects.filter(likes=self.request.user)

        # LIST ALL ACTIVE JOBS

        # JOBS USER NOT ENROLLED

        # GET LIKED JOBS ID

        # GET ENROLLED JOBS IDS

        context = super(HomeView, self).get_context_data(**kwargs)
        filter_object = JobFilter(self.request.GET, queryset=Job.objects.all())
        context['filter_form'] = filter_object.form

        paginator = Paginator(filter_object.qs, 50)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context['object_list'] = page_object
        return context


class ProjectView(DetailView):
    template_name = 'website/project_detail.html'
