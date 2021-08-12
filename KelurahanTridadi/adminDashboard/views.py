from django.shortcuts import render, redirect
from .forms import PostForm
from .models import *


# Create your views here.
def admindashboard(request):
    return render(request, 'adminDashboard/index.html')


def database(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/database/')

    warga = Warga.objects.all()
    context = {'form': form, 'warga': warga}

    return render(request, 'adminDashboard/database.html', context)


def deleteData(request, pk):
    warga = Warga.objects.get(id=pk)
    warga.delete()
    return redirect('/database/')
