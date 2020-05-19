from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Confession
from .serializers import ConfessionSerializer
from django.http import Http404
from rest_framework import generics

# Create your views here.

class ConfessionList(APIView):
    
    #List all code Articles, or create a new Article.
    def post(self, request, format=None):
        serializer = ConfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)