from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class UserDetails(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super(UserDetails, self).save(*args, **kwargs)

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('AP', 'Applied'),
        ('IN', 'Interview'),
        ('OF', 'Offer'),
        ('RE', 'Rejected'),
    ]

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    company = models.ManyToManyField(Company)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AP')
    date_applied = models.DateField(auto_created=True)
    modified = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comments = models.TextField(blank=True, null=True)


class Reminder(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    reminder_date = models.DateTimeField()
    message = models.TextField()
    is_active = models.BooleanField(default=True)
