from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response

from .serializers import UserSerializer, LoginSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST",])
def create(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    serializer.perform_create(serializer)
    return Response(serializer.data)
        
    # serializer.create()

@api_view(["POST",])
def login(request):
    
    serializer  = LoginSerializer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    email = serializer.data["email"]
    password = serializer.data["password"]
    
    user = authenticate(request=request,email=email, password=password)
    print("hello*********************", user, email, password)
    if user is None:
        return Response({
            "message": "enter valid email or password",
            }, status=status.HTTP_401_UNAUTHORIZED)
    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    })

# @api_view(["PUT"])
# def edit(request):
#     return HttpResponse("edit user ")
