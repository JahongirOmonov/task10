from django.urls import path 
from .views import allfunctions, ListQuestionView, createLeastQuestion, updateID, deleteID, DetailUniversityView,createLeastQuestionLIST
from .views import PostSumka, PatchSumka, DeleteSumka, GetAllSumka, PostGetSumka, GetDetailSumka, AllFunctionSumka
urlpatterns=[
    path('all/', ListQuestionView.as_view()),
    path('detail/<int:pk>', DetailUniversityView.as_view()),
    path('createLeastQuestionLIST/', createLeastQuestionLIST.as_view()),
    path('change/<int:pk>', updateID.as_view()),
        path('GetAllSumka/', GetAllSumka.as_view()),
    path('GetDetailSumka/<int:pk>', GetDetailSumka.as_view()),
    path('PostSumka/', PostSumka.as_view() ),
    path('PatchSumka/<int:pk>', PatchSumka.as_view()),
    path('DeleteSumka/<int:pk>', DeleteSumka.as_view()),
    path('PostGetSumka/', PostGetSumka.as_view()),
    path('AllFunctionSumka/<int:pk>', AllFunctionSumka.as_view()),
    path('delete/<int:pk>', deleteID.as_view()),
    path('allfunctions/<int:pk>', allfunctions.as_view())


]