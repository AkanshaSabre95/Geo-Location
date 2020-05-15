from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer
)
from .models import Customer

class AdSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Customer
        geo_field = 'location'
        fields = ('id')