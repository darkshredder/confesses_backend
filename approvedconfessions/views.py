from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Approvedconfessions
from .serializers import ApprovedconfessionSerializer
from django.http import Http404

# Create your views here.
class ApprovedconfessionsList(APIView):
    
    #List all code Articles, or create a new Article.

    def get(self,request,format=None):
        approvedconfessions = Approvedconfessions.objects.all()
        serializer = ApprovedconfessionSerializer(approvedconfessions, many=True)
        return Response(serializer.data)
