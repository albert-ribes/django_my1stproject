from django.db import models

# Create your models here.
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
 
    subject = models.CharField(max_length=200)
    message = models.TextField()
 
    created_date = models.DateTimeField(default=timezone.now)
    sent_date = models.DateTimeField(blank=True, null=True)

    def sent(self):
        self.sent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject

