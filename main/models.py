from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    contact = models.CharField(max_length=15)
    subject = models.CharField(max_length=122)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name