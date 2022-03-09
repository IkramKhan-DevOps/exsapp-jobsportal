from ckeditor.fields import RichTextField
from django.db import models

from src.accounts.models import User


class Company(models.Model):
    TYPE_CHOICE = (
        ('per', 'Personal'),
        ('pre', 'Premium'),
        ('ent', 'Enterprise'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Name")
    tag_line = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    business_type = models.CharField(max_length=255, choices=TYPE_CHOICE, default='per')

    contact_number = models.CharField(max_length=20, null=True, blank=True)
    contact_email = models.CharField(max_length=255, null=True, blank=True)
    contact_address = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# MODEL JOBS
class Job(models.Model):

    STATUS_CHOICE = (
        ('o', 'Open'),
        ('c', 'Close')
    )

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    detailed_description = RichTextField(null=True, blank=True)
    company = models.ForeignKey('Company', related_name='job_provider', on_delete=models.CASCADE, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes')
    candidates = models.ManyToManyField(User, related_name='candidates', through='Candidate')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='o')

    is_active = models.BooleanField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title


# CANDIDATE
class Candidate(models.Model):
    STATUS_CHOICE = (
        ('a', 'Accepted'),
        ('p', 'Pending'),
        ('c', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    cv = models.FileField(upload_to='company/candidates/files/')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title


# FEEDBACK
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company.name
