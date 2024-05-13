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
    
class UpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['first_name','last_name','company_name','address', 'phone_number', 'email', ]
        disallowed = ['password', ]
    
    def validate_email(self, value):
        # Check if the email already exists
        if Customer.objects.filter(email=value).exists():
            # If the email already exists, return the value instead of raising an error
            return value
    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        if validated_data.get("password") is None:
            instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
    