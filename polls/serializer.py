from rest_framework import serializers
from .models import university, sumka


# class universitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=university
#         fields=('name', 'filiallari', 'kantrakti')

class universitySerializer(serializers.ModelSerializer):
    class Meta:
        model=university
        fields=('__all__')




class sumkaSerializer(serializers.ModelSerializer):
    class Meta:
        model=sumka
        fields=('color', 'invented_country')