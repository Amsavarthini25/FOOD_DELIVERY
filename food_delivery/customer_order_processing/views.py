from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Registers a new customer with all details."""
    data = request.data
    if Customer.objects.filter(username=data['username']).exists():
        return Response({'error': 'Username already taken'}, status=400)

    user = Customer.objects.create_user(
        username=data['username'],
        password=data['password'],
        first_name=data.get('first_name', ''),
        last_name=data.get('last_name', ''),
        email=data.get('email', ''),
        address=data.get('address', ''),
        contact=data.get('contact', ''),
        payment_details=data.get('payment_details', ''),
        special_instructions=data.get('special_instructions', ''),  # Store special instructions
    )
    return Response({'message': 'User registered successfully!'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_customer_details(request):
    """Retrieve logged-in customer details."""
    customer = request.user
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_customer_details(request):
    """Update customer details."""
    customer = request.user
    serializer = CustomerSerializer(customer, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Customer details updated successfully!', 'data': serializer.data})
    return Response(serializer.errors, status=400)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Logs in an existing user."""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({'message': 'Login successful!'})
    return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    """Logs out the current user."""
    logout(request)
    return Response({'message': 'Logout successful!'})

