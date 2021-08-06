from django.urls import path
from .views import Chatroom

urlpatterns=[
    path('chatroom',Chatroom)
]