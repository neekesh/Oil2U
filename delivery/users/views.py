from django.contrib.auth import authenticate

from rest_framework.decorators import api_view,permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, LoginSerializer, UpdateUserSerializer,OrderSeralizer, UrgentDeliverySerializer,InvoiceSerializer,MaintainenceSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Customer


@api_view(["POST",])
def create(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    serializer.perform_create(serializer)
    return Response(serializer.data)

@api_view(["POST",])
def login(request):
    
    serializer  = LoginSerializer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    email = serializer.data["email"]
    password = serializer.data["password"]
    
    user = authenticate(request=request,email=email, password=password)
    if user is None:
        return Response({
            "message": "enter valid email or password",
            }, status=status.HTTP_401_UNAUTHORIZED)
    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    })

@api_view(['PUT'])  # Example permission class
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
@authentication_classes([JWTAuthentication])
def update_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateUserSerializer(customer, data=request.data)

    if serializer.is_valid():

        serializer.update(customer, validated_data=request.data)
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST",])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
@authentication_classes([JWTAuthentication])
def create_order(request):
    
    serializer  = OrderSeralizer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST",])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
@authentication_classes([JWTAuthentication])
def invoice(request):
    
    serializer  = InvoiceSerializer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET",])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
@authentication_classes([JWTAuthentication])
def all_invoices(request):
    
    serializer  = InvoiceSerializer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.Data, status=status.HTTP_201_CREATED)


@api_view(["GET",])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
@authentication_classes([JWTAuthentication])
def invoice_details(request):
    
    serializer  = InvoiceSerializer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(["POST",])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
@authentication_classes([JWTAuthentication])
def urgent_delivery(request):
    
    serializer  = UrgentDeliverySerializer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(["POST",])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
@authentication_classes([JWTAuthentication])
def maintainence(request):
    
     
    serializer  = MaintainenceSerializer(data =request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response(serializer.Data, status=status.HTTP_201_CREATED)