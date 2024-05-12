from rest_framework import serializers
from .models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = Customer
       fields= "__all__"
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
       

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()