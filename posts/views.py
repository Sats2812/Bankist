from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request,'index.html')


def account(request):
    print("this is req: ",request)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if new_user.objects.filter(username=username).exists():
            try:
                user = new_user.objects.get(username=username,password=password)
                if user.password == password:
                    print("the user password: ",user.password)
                    messages.info(request, '201')
                    return redirect("account")
                else: 
                    messages.info(request, 'username or password is wrong.')
                    return redirect("account")
            except:
                    messages.info(request, 'username or password is wrong.')
                    return redirect("account")

        else:
            messages.info(request, 'username or password is wrong.')
            return redirect("account")

    else:
        return render(request,'account.html')

def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if new_user.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('/')
            elif new_user.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('/')
            else:
                new=new_user(username=username, email=email, password=password,password2=password2)
                new.save()
                return redirect('account')
        else:
            messages.info(request,'Passwords not the same')
            return redirect('/')
    else: 
        return render(request,'notfound')

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        new_contact=contact(name=name,subject=subject,message=message,email=email)
        new_contact.save()
        message.info(request,'Thank you for contacting us , We will reach out to you soon')
        return redirect('contact')
    else:
        return render(request,'contact.html')


    
