from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Sky
from .serializers import SkySerializer

# Create your views here.

class SkyList(ListCreateAPIView):
    queryset = Sky.objects.all()
    serializer_class = SkySerializer

class SkyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Sky.objects.all()
    serializer_class = SkySerializer


