from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Confession
from .serializers import ConfessionSerializer
from django.http import Http404
from rest_framework import generics

# Create your views here.


class ConfessionList(generics.ListCreateAPIView):
    
    #List all code Articles, or create a new Article.

    queryset = Confession.objects.all()
    serializer_class = ConfessionSerializer
    

class ConfessionDetail(generics.RetrieveUpdateDestroyAPIView):
    #Retrieve, update or delete a Article.

    queryset = Confession.objects.all()
    serializer_class = ConfessionSerializer
    