from django.shortcuts import render, get_object_or_404
from .models import university, sumka
from django.http import JsonResponse
from .serializer import sumkaSerializer, universitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

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
# class ListQuestionView(APIView):
#     def get(self, request):
#         all_data = university.objects.all()
#         serializer=universitySerializer(all_data, many=True)
#         return Response(serializer.data)

class ListQuestionView(generics.ListAPIView):
    queryset=university.objects.all()
    serializer_class=universitySerializer

# def detail(request, forid):
#     some = get_object_or_404(sumka, id=forid)
#     # fornow = {'ranggi':some.color,'ishlab chiqarilgan mamlakat':some.invented_country}
#     # some=sumka.objects.filter(id=forid)
#     forsure=sumkaSerializer(some)
#     return JsonResponse(forsure.data, safe=False)
# class DetailUniversityView(APIView):
#     def get(self, request, *args, **kwargs):
#         some=get_object_or_404(university, id=kwargs['forid'])
#         foreha=universitySerializer(some)
#         return Response(foreha.data)

class DetailUniversityView(generics.RetrieveAPIView):
    queryset=university.objects.all()
    serializer_class=universitySerializer

# class DetailSumkaView(APIView):
#     def get(self, request, *args, **kwargs):
#         some=get_object_or_404(sumka, id=kwargs['forid'])
#         foreha=sumkaSerializer(some)
#         return Response(foreha.data)

# class createLeastQuestion(APIView):
#     def post(self, request):
#         # print(request.data)
#         user_body=request.data
#         serializer=universitySerializer(data=user_body)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
class createLeastQuestion(generics.CreateAPIView):
    queryset=university.objects.all()
    serializer_class=universitySerializer

class createLeastQuestionLIST(generics.ListCreateAPIView):
    queryset=university.objects.all()
    serializer_class=universitySerializer
                          
    
# class create2(APIView):
#     def post(self, request):
#         user_body=request.data
#         ushla=sumkaSerializer(data=user_body)
#         if ushla.is_valid():
#             ushla.save()
#             return Response(ushla.data)
#         return Response(ushla.errors)
class GetAllSumka(generics.ListAPIView):
    queryset=sumka.objects.all()
    serializer_class=sumkaSerializer

class GetDetailSumka(generics.RetrieveAPIView):
    queryset = sumka.objects.all()
    serializer_class=sumkaSerializer

class PostSumka(generics.CreateAPIView):
    queryset=sumka.objects.all()
    serializer_class=sumkaSerializer

class PatchSumka(generics.UpdateAPIView):
    queryset=sumka.objects.all()
    serializer_class=sumkaSerializer

class DeleteSumka(generics.DestroyAPIView):
    queryset=sumka.objects.all()
    serializer_class=sumkaSerializer

class PostGetSumka(generics.ListCreateAPIView):
    queryset=sumka.objects.all()
    serializer_class=sumkaSerializer

class AllFunctionSumka(generics.RetrieveUpdateDestroyAPIView):
    queryset=sumka.objects.all()
    serializer_class=sumkaSerializer
    
# class updateID(APIView):
#     def patch(self, request, *args, **kwargs):
#         question=get_object_or_404(university, id=kwargs['forid'])
#         serzzz=universitySerializer(question, data=request.data, partial=True)
#         if serzzz.is_valid():
#             serzzz.save()
#             return Response(serzzz.data)
#         return Response(serzzz.errors)

class updateID(generics.UpdateAPIView):
    queryset=university.objects.all()
    serializer_class=universitySerializer

    
# class deleteID(APIView):
#     def delete(self, request, *args, **kwargs):
#         cc=get_object_or_404(university, id=kwargs['forid'])
#         cc.delete()
#         return Response({"msg":'succesfully deleted'})

class deleteID(generics.DestroyAPIView):
    queryset=university.objects.all()
    serializer_class=universitySerializer

class allfunctions(generics.RetrieveUpdateDestroyAPIView):
    queryset=university.objects.all()
    serializer_class=universitySerializer

    


        
