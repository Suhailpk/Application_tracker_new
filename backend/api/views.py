from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def test(request):
    return HttpResponse('<h1>Hello<h1/>')


class UserView(ViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerailzer

    def list(self, request):
        queryset = UserDetails.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        print("username from register view --------->", username)
        print("email from register view --------->", email)
        print("password from register view --------->", password)

        try:
            # Create a new user with a hashed password
            user = User(username=username, email=email)
            user.set_password(password)  # This hashes the password
            user.save()
        except Exception as e:
            print("there is error for saving the user registration form ------>", e)

        return Response({"success":"Succefully reigster the user"}, status=status.HTTP_200_OK)
        


class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        print("username from frontend --------->", username)
        print("password from frontend --------->", password)

        user = authenticate(request, username=username, password=password)

        print("user ------>",   user)

        if user is not None:
            print("user is not none")
            login(request, user)
            print("the current user is ---------->", request.user)
            return Response({'message':'Successfully Logged the user'}, status=status.HTTP_200_OK)
            
        else:
            print("there is a problem in user")
            return Response({'error':'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        

class ProtectedView(APIView, LoginRequiredMixin):
    login_url = '/login/'

    def get(self, request):
        if request.user.is_authenticated:
            print("user is authenticated")
        else:
            print("not authenticated")
        return Response({'message': 'This is a protected view!'}, status=status.HTTP_200_OK)
    
        

def test_code(username, email, password):
    print("------------- working the test code -----------")
    from django.contrib.auth.models import User

    try:
        # Create a new user with a hashed password
        user = User(username=username, email=email)
        user.set_password(password)  # This hashes the password
        user.save()
    except Exception as e:
        print("there is error for saving the user registration form ------>", e)

       
        
        

