from django.urls import path
from . import views


urlpatterns = [
    path('', GetQuestion.as_view()),
    path('answer/', QuestionAnswer.as_view()),
]