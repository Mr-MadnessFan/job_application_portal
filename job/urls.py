from django.urls import path
from .views import HomePage, CategoryPage, jobs_detail, OfflineCategoryPage, HybridCategoryPage, UpdateJobsView, \
    DeleteJobsView, CreateJobsView

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('online-jobs-category/', CategoryPage.as_view(), name='online_category_page'),
    path('create-vacancy/', CreateJobsView.as_view(), name='create_page'),
    path('offline-jobs-category/', OfflineCategoryPage.as_view(), name='offline_category_page'),
    path('hybrid-jobs-category/', HybridCategoryPage.as_view(), name='hybrid_category_page'),
    path('<slug:slug>/', jobs_detail, name='jobs_details'),
    path('<slug:slug>/update', UpdateJobsView.as_view(), name='update_page'),
    path('<slug:slug>/delete', DeleteJobsView.as_view(), name='delete_page')
]