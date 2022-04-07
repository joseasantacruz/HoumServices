from rest_framework import serializers
from .models import Coordinates

class CoordinatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ['id', 'houmer_id', 'lat','lon','created_on']
