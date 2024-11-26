from django.shortcuts import render
from .serializers import TrainSerializer
from .models import New_Joinee
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse


# Create your views here.


def view_trainee(request):
    if request.method=='GET':
        trainees =  New_Joinee.objects.all()
        serializer = TrainSerializer(trainees,many=True)
        return JsonResponse(serializer.data)
    
