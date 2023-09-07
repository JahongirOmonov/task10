from django.urls import path 
from .views import ListQuestionView, DetailSumkaView, createLeastQuestion, create2

urlpatterns=[
    path('all/', ListQuestionView.as_view()),
    path('detail/<int:forid>', DetailSumkaView.as_view()),
    path('create/', createLeastQuestion.as_view()),
    path('create2/', create2.as_view())
]