from django.urls import path
from .views import home, ask_question, answer_question

urlpatterns = [
    path('', home, name='home'),
    path('ask/', ask_question, name='ask_question'),
    path('answer/<int:question_id>/', answer_question, name='answer_question'),
]
