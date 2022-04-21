from django.urls import path
from f1.views import *
urlpatterns = [
    path('', index),
    path('schedule/', F1SchedulesView.as_view()),
]
