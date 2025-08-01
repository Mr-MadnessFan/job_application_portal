from django.contrib import admin

from job.models import PodCategory, Category, Jobs, WorkingKnowledge, WorksSchedule, WorkingTime, WorkFormat


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('id','title','author')
    prepopulated_fields = {'slug':('title',)}

@admin.register(PodCategory)
class PodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(WorkingKnowledge)
class WorkingKnowledgeAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(WorksSchedule)
class WorksScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(WorkingTime)
class WorkingTimeAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(WorkFormat)
class WorkFormatAdmin(admin.ModelAdmin):
    list_display = ('id','name')