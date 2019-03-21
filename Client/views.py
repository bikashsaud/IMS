from django.shortcuts import render,redirect
# from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ClientForm,ClientLoginForm
from .forms import AgentForm,AgentLoginForm
from .models import Client
from Agent.models import Agent
from datetime import date
from django.contrib import messages

# Create your views here.
# @login_required
def client_login(request):
    form=ClientLoginForm(request.POST or None)
    if request.method=='POST' or None:

        form_no=request.POST.get('Form_number')
        email=request.POST.get('Email')
        data=Client.objects.get(Form_number=form_no)
        if str(data.Form_number) == str(form_no):
            context={'data':data,}
            return render(request,'client_detail.html',context)
        else:
            return redirect('client_login')
    context={"form":form,}
    return render(request,"client_login.html",context)

def client_detail(request):
    return HttpResponse("<h1>Bikash Saud </h1>")
    # form=Client.objects.get(id=id)
    # context={"form":form,}
    # return render(request,"client_detail.html",)

def agent_login(request):
    form=AgentLoginForm(request.POST or None)
    if request.method =='POST' or None:
        email=request.POST.get('Email')
        license_code=request.POST.get("License_code")
        data=Agent.objects.get(License_code=license_code)
        if str(data.License_code)==str(license_code):
            context={"data":data,}
            return render(request,'agent_detail.html',context)
        else:
            return redirect('agent_login')
    context={'form':form,}
    return render(request,'agent_login.html',context)

def register_client(request):
    # aform=AgentForm(request.POST or None)
    form=ClientForm(request.POST or None)
    if form.is_valid():
        # aform.save() or
        form.save()
        return redirect('index')
    context={"form":form,}
    return render(request,'client_register.html',context)
def register_agent(request):
    aform=AgentForm(request.POST or None)

    if aform.is_valid():
        aform.save()
        # form.save()
        return redirect('index')
    context={'aform':aform,}
    return render(request,'agent_register.html',context)

def add_policy(request,id):
    return HttpResponse("<h2>POLICY DETAIL IS HERE</h2>")
