from django.urls import path
from .views import *

urlpatterns = [
    path('', get_machine_learning_news, name='get_machine_learning_news'),
]
