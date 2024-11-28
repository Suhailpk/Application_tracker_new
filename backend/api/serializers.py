from rest_framework import serializers
from .models import *
from core.models import User
# from django.contrib.auth.models import User


# class UserSerailzer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')


class RegisterSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password1', 'password2', 'email', 'first_name', 'last_name']




from core.models import User

class AddNewApplicationSerailzer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)  # The user field will just hold the ID
    company_id = serializers.IntegerField()
    company_name = serializers.SerializerMethodField()
    status_full = serializers.SerializerMethodField()

    class Meta:
        model = JobApplication
        fields = ('id', 'user_id', 'company_id', 'company_name', 'position', 'status', 'status_full', 'salary', 'comments')


    def get_company_name(self, obj):
        company = Company.objects.filter(id=obj.company_id).first()
        return company.name if company else None
    
    def get_status_full(self, obj):
        return dict(JobApplication.STATUS_CHOICES).get(obj.status)

    def create(self, validated_data):
        user_id = self.context["user_id"]  # Get the user_id from the context
        # Create the JobApplication instance
        job_application = JobApplication.objects.create(user_id=user_id, **validated_data)
        # Set the companies to the job application
        job_application.save()

        return job_application
    


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'website', 'industry')


