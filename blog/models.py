from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True)
    snippet = models.TextField(max_length=600, blank=True)
    image = RichTextUploadingField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_boolean = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    


class Solution(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True)
    snippet = models.TextField(max_length=600, blank=True)
    image = RichTextUploadingField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_boolean = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    


class ReleaseNotes(models.Model):
    title = models.CharField(max_length=300) 
    author = models. ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = RichTextField()
    snippet = models.TextField(max_length=600, blank=True)
    image = RichTextUploadingField(blank=True)
    publish_boolean = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    


class JobPost(models.Model):
    title = models.CharField(max_length=300, blank=True)
    date_posted = models.DateTimeField(default=timezone.now, blank=True)
    salary = models.CharField(max_length=300, blank=True)
    start_date = models.CharField(max_length=300, blank=True)
    duration = models.CharField(max_length=300, blank=True)
    location = models.CharField (max_length=300, blank=True)
    job_description = RichTextField()
    job_requirements = RichTextField()
    publish_boolean = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    


class JobApplication(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=500)
    jobpost = models.ForeignKey(JobPost, on_delete=models.SET_NULL, null=True, blank=True, related_name='jobapplication')
    subject = models.CharField(max_length=500, blank=True)
    message = models.TextField(max_length=10000, blank=True)
    resume_upload = models.FileField(upload_to='media/job_application_files/', validators=[
        FileExtensionValidator(allowed_extensions=['pdf'])
    ])

    def __str__(self):
        return f"{self.jobpost} - {self.email}"



class ContactRequest(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    subject = models.CharField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    def __str__(self):
        return self.subject
    


class NewsletterRequest(models.Model):
    email = models.CharField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
    
    

class NewsletterUnsubscribeRequest(models.Model):
    email = models.CharField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email



class Resource(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='media/resources/')
    uploaded_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name



