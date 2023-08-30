from django.shortcuts import render, get_object_or_404
from .models import university, sumka
from django.http import JsonResponse

# Create your views here.

def all(request):
    pustoy=[]
    each = university.objects.all()
    for i in each:
        pustoy.append({
            'Universitet nomi':i.name,
            'Universitet filillari':i.filiallari,
            'Universitet kantrakti':i.kantrakti
        })
    return JsonResponse(pustoy, safe=False)

def detail(request, forid):
    some = get_object_or_404(sumka, id=forid)
    fornow = {'ranggi':some.color,'ishlab chiqarilgan mamlakat':some.invented_country}
    return JsonResponse(fornow, safe=False)
