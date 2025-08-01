from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Jobs, PodCategory, Category

def jobs_detail(request, slug):
    jobs = get_object_or_404(Jobs, slug=slug, status=Jobs.Status.Published)
    job = Jobs.published.all()
    context = {
        "jobs":jobs,
        "job":job
    }
    return render(request, 'details.html', context)

class HomePage(ListView):
    model = Jobs
    template_name = 'index.html'
    context_object_name = 'jobs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs_40'] = Jobs.published.order_by('-publish_time')[:53]
        context['jobs_6'] = Jobs.published.order_by('-publish_time')[:6]
        context['jobs_15'] = Jobs.published.order_by('-publish_time')[:22]
        context['subcategory'] = PodCategory.objects.all()
        context['category'] = Category.objects.all()

        return context

class CategoryPage(ListView):
    model = Jobs
    template_name = 'online_jobs_category.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Jobs.published.all().filter(work_format__name='online')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = self.get_queryset()
        category = Category.objects.all()
        subcategory = PodCategory.objects.all()
        paginator = Paginator(jobs, 6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context.update({
            'jobs': page_obj.object_list,
            'page_obj': page_obj,
            'category':category,
            'subcategory': subcategory
        })
        return context

class OfflineCategoryPage(ListView):
    model = Jobs
    template_name = 'offline_jobs_category.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Jobs.published.all().filter(work_format__name='offline')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = self.get_queryset()
        category = Category.objects.all()
        subcategory = PodCategory.objects.all()
        paginator = Paginator(jobs, 6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context.update({
            'jobs': page_obj.object_list,
            'page_obj': page_obj,
            'category':category,
            'subcategory': subcategory
        })
        return context

class HybridCategoryPage(ListView):
    model = Jobs
    template_name = 'hybrid_jobs.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return Jobs.published.all().filter(work_format__name='hybrid')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jobs = self.get_queryset()
        category = Category.objects.all()
        subcategory = PodCategory.objects.all()
        paginator = Paginator(jobs, 6)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context.update({
            'jobs': page_obj.object_list,
            'page_obj': page_obj,
            'category':category,
            'subcategory': subcategory
        })
        return context


class UpdateJobsView(UpdateView):
    model = Jobs
    fields = ('title', 'slug', 'payment', 'company', 'work_schedule', 'working_time', 'work_format',
              'working_knowledge','body', 'image', 'category', 'need_category', 'contact', 'email',
              'address')
    template_name = 'crud/update.html'

class DeleteJobsView(DeleteView):
    model = Jobs
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('home_page')

class CreateJobsView(CreateView):
    model = Jobs
    fields = ('title', 'slug', 'payment', 'company', 'work_schedule', 'working_time', 'work_format',
              'working_knowledge', 'body', 'image', 'category', 'need_category', 'contact', 'email',
              'address')
    template_name = 'crud/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




