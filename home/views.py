from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def home(request):
    context = {
        'data': Desgination.objects.all()
    }
    return render(request,'index.html', context=context)


def search_train(request):

    data = request.POST
    frm = Desgination.objects.get(id = data['frm'])
    to = Desgination.objects.get(id = data['to'])

    available_train = Schedule.objects.filter(frm = frm, to = to)

    context = {
        'available_train' : available_train
    }
    return render(request,'train_details.html', context=context)