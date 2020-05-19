from rest_framework import serializers
from .models import Approvedconfessions


class ApprovedconfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approvedconfessions
        fields = '__all__'
