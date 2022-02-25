from ckeditor.fields import RichTextField
from django.db import models


# MODEL CATEGORY
from src.accounts.models import User


class Company(models.Model):
    TYPE_CHOICE = (
        ('per', 'Personal'),
        ('pre', 'Premium'),
        ('ent', 'Enterprise'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tag_line = models.CharField(max_length=255)
    description = models.TextField()
    business_type = models.CharField(max_length=255, choices=TYPE_CHOICE)

    contact_number = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=255)
    contact_address = models.TextField()

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
    detailed_description = RichTextField()
    company = models.ForeignKey('Company', related_name='job_provider', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    likes = models.ManyToManyField(User, related_name='likes')
    candidates = models.ManyToManyField(User, related_name='candidates', through='Candidate')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)

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
