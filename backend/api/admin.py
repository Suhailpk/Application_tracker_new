from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Company)
admin.site.register(JobApplication)
admin.site.register(Reminder)