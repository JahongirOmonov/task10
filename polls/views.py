from django.shortcuts import render, get_object_or_404
from .models import university, sumka
from django.http import JsonResponse
from .serializer import sumkaSerializer, universitySerializer

# Create your views here.

def all(request):
    each = university.objects.all()
    pustoy=universitySerializer(each, many=True)
    # for i in each:
    #     pustoy.append({
    #         'Universitet nomi':i.name,
    #         'Universitet filillari':i.filiallari,
    #         'Universitet kantrakti':i.kantrakti
    #     })
    return JsonResponse(pustoy.data, safe=False)

def detail(request, forid):
    # some = get_object_or_404(sumka, id=forid)
    # fornow = {'ranggi':some.color,'ishlab chiqarilgan mamlakat':some.invented_country}
    some=sumka.objects.filter(id=forid)
    forsure=sumkaSerializer(some, many=True)
    return JsonResponse(forsure.data, safe=False)
