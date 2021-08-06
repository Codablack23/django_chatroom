from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth  import login

# Create your views here.
def Signup(request):
    if request.method =="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    else:
        form=UserCreationForm()

    return render(request,'accounts/signup.html',{'form':form})
    

def Login(request):
  

    if request.method =="POST":
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/chatroom')
    else:
        form=AuthenticationForm()


    return render(request,'accounts/login.html',{'title':'Log In','form':form})