from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import  UserRegistrationSerializer,UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes, permission_classes



@authentication_classes([])  # No authentication required
@permission_classes([])  
class UserRegistrationView(APIView):
  @csrf_exempt
  def post(self, request, format=None):
    """
    Handles POST requests for user registration.
    """
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({ 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    
      
       
      
@authentication_classes([])  # No authentication required
@permission_classes([])  
class UserLoginView(APIView):
  def post(self, request, format=None):
    """
    Handles POST requests for user login with credential(username/email/mobile).
    """
    serializer = UserLoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data
    return Response({'token': data['token'], 'msg': 'Login Success'}, status=status.HTTP_200_OK)
    
    
