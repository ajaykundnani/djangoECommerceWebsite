

from django.db.models import fields
from rest_framework import serializers
from .models import Users

class UsersSerializers(serializers.ModelSerializer):
    u_name = serializers.CharField(required = False)
    u_pass = serializers.CharField(required = False)
    u_email = serializers.CharField(required = False)
    class Meta:
        model = Users
        fields = '__all__'