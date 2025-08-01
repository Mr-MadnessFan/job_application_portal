from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Jobs.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkFormat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkingTime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorksSchedule(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkingKnowledge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PodCategory(models.Model):
    name = models.CharField(max_length=100)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategory'


class Jobs(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', "Draft"
        Published = 'PB', 'Published'
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    payment = models.CharField(max_length=300)
    company = models.CharField(max_length=100)
    work_schedule = models.ForeignKey(WorksSchedule, on_delete=models.CASCADE)
    working_time = models.ForeignKey(WorkingTime, on_delete=models.CASCADE)
    work_format = models.ForeignKey(WorkFormat, on_delete=models.CASCADE)
    working_knowledge = models.ForeignKey(WorkingKnowledge, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    need_category = models.ForeignKey(PodCategory, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to='jobs/%Y/%m/%d')
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'job'
        verbose_name_plural = 'jobs'

    def __str__(self):
        return self.title

    def clean(self):
        if self.need_category.main_category != self.category:
            raise ValidationError(f"{self.need_category} {self.category}ga kirmaydi.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('jobs_details', args=[self.slug])







