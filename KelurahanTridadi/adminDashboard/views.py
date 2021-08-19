from django.db.models import Count
from django.shortcuts import render, redirect
from .forms import PostForm, UpdateForm, PenangananForm
from .models import *


# Create your views here.
def admindashboard(request):
    konfirmasi_count_perday = Warga.objects.all() \
        .extra({'date_created': "date(tanggal_input)"}) \
        .values('date_created') \
        .annotate(created_count=Count('id'))

    isoman_count_perday = Warga.objects.filter(status='Isolasi Mandiri') \
        .extra({'date_created': "date(tanggal_penanganan)"}) \
        .values('date_created') \
        .annotate(created_count=Count('id'))

    sembuh_count_perday = Warga.objects.filter(status='Sembuh') \
        .extra({'date_created': "date(tanggal_penanganan)"}) \
        .values('date_created') \
        .annotate(created_count=Count('id'))

    meninggal_count_perday = Warga.objects.filter(status='Meninggal') \
        .extra({'date_created': "date(tanggal_penanganan)"}) \
        .values('date_created') \
        .annotate(created_count=Count('id'))

    dirawat_count_perday = Warga.objects.filter(status='Dirawat') \
        .extra({'date_created': "date(tanggal_penanganan)"}) \
        .values('date_created') \
        .annotate(created_count=Count('id'))

    konfirmasi_count = Warga.objects.all().count
    isoman_count = Warga.objects.filter(status='Isolasi Mandiri').count
    sembuh_count = Warga.objects.filter(status='Sembuh').count
    meninggal_count = Warga.objects.filter(status='Meninggal').count
    dirawat_count = Warga.objects.filter(status='Dirawat').count

    Wadas = Warga.objects.filter(padukuhan='Wadas').count
    Paten = Warga.objects.filter(padukuhan='Paten').count
    Ngemplak = Warga.objects.filter(padukuhan='Ngemplak Caban').count
    Pangukan = Warga.objects.filter(padukuhan='Pangukan').count
    Beteng = Warga.objects.filter(padukuhan='Beteng').count
    Pisangan = Warga.objects.filter(padukuhan='Pisangan').count
    Dukuh = Warga.objects.filter(padukuhan='Dukuh').count
    Beran_lor = Warga.objects.filter(padukuhan='Beran Lor').count
    Josari = Warga.objects.filter(padukuhan='Josari').count
    Drono = Warga.objects.filter(padukuhan='Drono').count
    Beran_kidul = Warga.objects.filter(padukuhan='').count
    Kebonagung = Warga.objects.filter(padukuhan='Kebonagung').count
    Jaban = Warga.objects.filter(padukuhan='Jaban').count
    Denggung = Warga.objects.filter(padukuhan='Denggung').count
    Bangunrejo = Warga.objects.filter(padukuhan='Bangunrejo').count

    padukuhan_list = (Wadas,
                      Paten,
                      Ngemplak,
                      Pangukan,
                      Beteng,
                      Pisangan,
                      Dukuh,
                      Beran_lor,
                      Josari,
                      Drono,
                      Beran_kidul,
                      Kebonagung,
                      Jaban,
                      Denggung,
                      Bangunrejo)

    context = {
        'count_perday': konfirmasi_count_perday,
        'isoman_perday': isoman_count_perday,
        'sembuh_perday': sembuh_count_perday,
        'meninggal_perday': meninggal_count_perday,
        'dirawat_perday': dirawat_count_perday,
        'total_count': konfirmasi_count,
        'isoman_count': isoman_count,
        'sembuh_count': sembuh_count,
        'meninggal_count': meninggal_count,
        'dirawat_count': dirawat_count,
        'padukuhan': padukuhan_list
    }
    return render(request, 'adminDashboard/index.html', context)


def database(request):
    warga = Warga.objects.all()
    context = {'warga': warga}

    return render(request, 'adminDashboard/database.html', context)


def dataform(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/database/')

    context = {'form': form}

    return render(request, 'adminDashboard/data_form.html', context)


def updatedata(request, pk):
    warga = Warga.objects.get(id=pk)
    form = UpdateForm(instance=warga)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=warga)
        if form.is_valid():
            form.save()
            return redirect('/database/')

    context = {'form': form}

    return render(request, 'adminDashboard/update_form.html', context)


def penanganandata(request, pk):
    warga = Warga.objects.get(id=pk)
    form = PenangananForm(instance=warga)
    if request.method == "POST":
        form = PenangananForm(request.POST, instance=warga)
        print("TESTING", form.is_valid())
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/database')

    context = {'form': form}

    return render(request, 'adminDashboard/penanganan_form.html', context)


def deleteData(request, pk):
    warga = Warga.objects.get(id=pk)
    warga.delete()
    return redirect('/database/')
