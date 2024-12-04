from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        pass

    else:
        return redirect('/')
    

def register_view(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        pass

    else:
        return redirect('/')