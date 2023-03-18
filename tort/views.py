from rest_framework.viewsets import ModelViewSet

from .models import Airport, Company
from .serializers import AirportSerializer, CompanySerializer


class AirportViewSet(ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

