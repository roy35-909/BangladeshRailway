from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .models import User
from django.contrib import messages



def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        data = request.POST

        user = User.objects.filter(phone = data['phone'])
        if user.exists():
            user = user.first()
            user = authenticate(username = user.username, password = data['password'])
            if user is None:
                messages.error(request,"Invalid Password")
                return redirect("/auth/login/")
            else:
                login(request, user)
                return redirect('/')
        else:
            messages.error(request,"Invalid Phone")
            return redirect("/auth/login/")
    else:
        return redirect('/')
    

def register_view(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        data= request.POST

        user = User.objects.create(username=data['phone'],email = data['email'], first_name = data['name'], phone=data["phone"])
        user.set_password(data['password'])
        user.save()
        return redirect('/auth/login/')

    else:
        return redirect('/')
    

def user_logout(request):
    logout(request)
    return redirect('/')