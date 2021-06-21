from rest_framework import serializers
from .models import Sky

class SkySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sky
        fields = ('id','name', 'discription', 'architect')