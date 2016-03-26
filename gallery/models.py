from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.utils import timezone

# Helper functions for images
def get_image_path(instance, filename):
    return '/'.join(['work_images', instance.work.slug, filename])

class Work(models.Model):
    
    STATUS_TYPES = (
        ('pending','Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
    
    title = models.CharField(max_length=64)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    submit_date = models.DateTimeField(default=timezone.now)
    approved_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_TYPES, default=STATUS_TYPES[0])
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def approve(self):
        self.approved_date = timezone.now()
        self.status = STATUS_TYPES[1]
        self.save()
        
    def reject(self):
        self.status = STATUS_TYPES[2]
        self.save()
        
    def __str__(self):
        return self.title

    
    
class Upload(models.Model):
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    work = models.ForeignKey(Work, related_name="uploads")