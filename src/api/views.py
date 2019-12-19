from rest_framework import viewsets 

from .models import Sample
from .serializers import SampleSerializer

class SampleViewSet(viewsets.ModelViewSet): 
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer 
