from rest_framework import serializers
from .models import university, sumka
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 


# class universitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=university
#         fields=('name', 'filiallari', 'kantrakti')

class universitySerializer(serializers.ModelSerializer):
    class Meta:
        model=university
        fields=('__all__')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(universitySerializer, self).create(validated_data)




class sumkaSerializer(serializers.ModelSerializer):
    class Meta:
        model=sumka
        fields=('color', 'invented_country')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(sumkaSerializer, self).create(validated_data)