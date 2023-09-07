from django.shortcuts import render, get_object_or_404
from .models import university, sumka
from django.http import JsonResponse
from .serializer import sumkaSerializer, universitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def all(request):
#     each = university.objects.all()
#     pustoy=universitySerializer(each, many=True)
#     # for i in each:
#     #     pustoy.append({
#     #         'Universitet nomi':i.name,
#     #         'Universitet filillari':i.filiallari,
#     #         'Universitet kantrakti':i.kantrakti
#     #     })
#     return JsonResponse(pustoy.data, safe=False)
class ListQuestionView(APIView):
    def get(self, request):
        all_data = university.objects.all()
        serializer=universitySerializer(all_data, many=True)
        return Response(serializer.data)

# def detail(request, forid):
#     some = get_object_or_404(sumka, id=forid)
#     # fornow = {'ranggi':some.color,'ishlab chiqarilgan mamlakat':some.invented_country}
#     # some=sumka.objects.filter(id=forid)
#     forsure=sumkaSerializer(some)
#     return JsonResponse(forsure.data, safe=False)

class DetailSumkaView(APIView):
    def get(self, request, *args, **kwargs):
        some=get_object_or_404(sumka, id=kwargs['forid'])
        foreha=sumkaSerializer(some)
        return Response(foreha.data)

class createLeastQuestion(APIView):
    def post(self, request):
        # print(request.data)
        user_body=request.data
        serializer=universitySerializer(data=user_body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class create2(APIView):
    def post(self, request):
        user_body=request.data
        ushla=sumkaSerializer(data=user_body)
        if ushla.is_valid():
            ushla.save()
            return Response(ushla.data)
        return Response(ushla.errors)


        
