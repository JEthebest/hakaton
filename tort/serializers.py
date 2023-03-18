from rest_framework import serializers

from .models import Airport, Company

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = (
            'iata_code',
            'name'
        )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'iata_code',
            'name'
        )