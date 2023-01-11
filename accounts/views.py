from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser 
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.request import Request

from accounts.serializer import RegisterSerializer

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response =  {
                "message": "User created sucessfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




