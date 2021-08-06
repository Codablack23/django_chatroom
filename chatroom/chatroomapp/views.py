import django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def Chatroom(request):
    return render(request,'chat/chatroom.html',{'title':'Chatroom'})