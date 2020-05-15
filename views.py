
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from .models import Customer
from .serializers import AdSerializer
from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.

class AdViewSet(ReadOnlyModelViewSet):
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter,)
    queryset = Customer.objects.filter(location__isnull = False)
    serializer_class = AdSerializer

def index(request):
    return render(request,'Network/index.html')