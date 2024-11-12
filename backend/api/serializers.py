from rest_framework import serializers
from .models import *


class UserSerailzer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id', 'username', 'email', 'password')