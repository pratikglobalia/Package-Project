from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import *
from .serializers import *

def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class RegisterApiView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data Register Successfully!!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response({'invalid username or password'}, status= status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyActivityView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        myactivity = Activity.objects.filter(user=request.user)
        serializer = ActivitySerializer(myactivity, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        userpackage = PurchasePackage.objects.filter(user=request.user).last()
        if userpackage:
            useractivity = Activity.objects.filter(user=request.user, package=userpackage.package)
            totalactivity = userpackage.package.total_activity
            if useractivity.count() < totalactivity:
                serializer = ActivitySerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save(user=request.user, package=userpackage.package)
                    return Response({'Data Created!!!'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'You reached your package limit!, Please purchase package!!'})
        return Response({'You have no package!, Please purchase!!!'})

        
class AllActivityView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, format=None):
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PurchasePackageView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = PurchasePackageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)