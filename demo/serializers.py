from rest_framework import serializers
from .models import New_Joinee

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_Joinee