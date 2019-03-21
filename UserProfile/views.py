from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserLoginForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .models import UserProfile
User=get_user_model()
# Create your views here.
@login_required
def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context={"form":form,}
    return render(request,'register.html',context)

def signin(request):
    form= UserLoginForm(request.POST or None)
    if form.is_valid():
        user=User.objects.get(email__iexact=form.cleaned_data.get('email'))
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    con={'con':form,}
    return render(request,'login.html',con)
@login_required
def signout(request):
    logout(request)
    return redirect('login')
