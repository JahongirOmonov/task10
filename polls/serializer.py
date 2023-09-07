from rest_framework import serializers
from .models import university, sumka


class universitySerializer(serializers.ModelSerializer):
    class Meta:
        model=university
        fields=('name', 'filiallari', 'kantrakti')




class sumkaSerializer(serializers.ModelSerializer):
    class Meta:
        model=sumka
        fields=('color', 'invented_country')