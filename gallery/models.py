from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Work(models.Model):
    
    STATUS_TYPES = (
        ('pending','Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    )
    
    title = models.CharField(max_length=64)
    description = models.TextField()
    submit_date = models.DateTimeField(default=timezone.now)
    approved_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_TYPES, default=STATUS_TYPES[0][0])
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='work_images/%Y/%m/%d')
    
    def approve(self):
        self.approved_date = timezone.now()
        self.status = self.STATUS_TYPES[1][0]
        self.save()
        
    def reject(self):
        self.status = self.STATUS_TYPES[2][0]
        self.save()
        
    def __str__(self):
        return self.title
    