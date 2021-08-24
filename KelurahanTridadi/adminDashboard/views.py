from django.db.models import Count
from django.shortcuts import render, redirect
from .forms import PostForm, UpdateForm, PenangananForm
from .models import *

from django.contrib.auth.decorators import login_required


@login_required
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
    Beran_kidul = Warga.objects.filter(padukuhan='Beran Kidul').count
    Kebonagung = Warga.objects.filter(padukuhan='Kebonagung').count
    Jaban = Warga.objects.filter(padukuhan='Jaban').count
    Denggung = Warga.objects.filter(padukuhan='Denggung').count
    Bangunrejo = Warga.objects.filter(padukuhan='Bangunrejo').count

    wadas_dirawat = Warga.objects.filter(padukuhan='Wadas', status='Dirawat').count
    paten_dirawat = Warga.objects.filter(padukuhan='Paten', status='Dirawat').count
    ngemplak_dirawat = Warga.objects.filter(padukuhan='Ngemplack Caban', status='Dirawat').count
    pangukan_dirawat = Warga.objects.filter(padukuhan='Pangukan', status='Dirawat').count
    beteng_dirawat = Warga.objects.filter(padukuhan='Beteng', status='Dirawat').count
    pisangan_dirawat = Warga.objects.filter(padukuhan='Pisangan', status='Dirawat').count
    dukuh_dirawat = Warga.objects.filter(padukuhan='Dukuh', status='Dirawat').count
    beranlor_dirawat = Warga.objects.filter(padukuhan='Beran Lor', status='Dirawat').count
    josari_dirawat = Warga.objects.filter(padukuhan='Josari', status='Dirawat').count
    drono_dirawat = Warga.objects.filter(padukuhan='Drono', status='Dirawat').count
    berankidul_dirawat = Warga.objects.filter(padukuhan='Beran Kidul', status='Dirawat').count
    kebonagung_dirawat = Warga.objects.filter(padukuhan='Kebonagung', status='Dirawat').count
    jaban_dirawat = Warga.objects.filter(padukuhan='Jaban', status='Dirawat').count
    denggung_dirawat = Warga.objects.filter(padukuhan='Denggung', status='Dirawat').count
    bangunrejo_dirawat = Warga.objects.filter(padukuhan='Bangunrejo', status='Dirawat').count

    wadas_isoman = Warga.objects.filter(padukuhan='Wadas', status='Isolasi Mandiri').count
    paten_isoman = Warga.objects.filter(padukuhan='Paten', status='Isolasi Mandiri').count
    ngemplak_isoman = Warga.objects.filter(padukuhan='Ngemplack Caban', status='Isolasi Mandiri').count
    pangukan_isoman = Warga.objects.filter(padukuhan='Pangukan', status='Isolasi Mandiri').count
    beteng_isoman = Warga.objects.filter(padukuhan='Beteng', status='Isolasi Mandiri').count
    pisangan_isoman = Warga.objects.filter(padukuhan='Pisangan', status='Isolasi Mandiri').count
    dukuh_isoman = Warga.objects.filter(padukuhan='Dukuh', status='Isolasi Mandiri').count
    beranlor_isoman = Warga.objects.filter(padukuhan='Beran Lor', status='Isolasi Mandiri').count
    josari_isoman = Warga.objects.filter(padukuhan='Josari', status='Isolasi Mandiri').count
    drono_isoman = Warga.objects.filter(padukuhan='Drono', status='Isolasi Mandiri').count
    berankidul_isoman = Warga.objects.filter(padukuhan='Beran Kidul', status='Isolasi Mandiri').count
    kebonagung_isoman = Warga.objects.filter(padukuhan='Kebonagung', status='Isolasi Mandiri').count
    jaban_isoman = Warga.objects.filter(padukuhan='Jaban', status='Isolasi Mandiri').count
    denggung_isoman = Warga.objects.filter(padukuhan='Denggung', status='Isolasi Mandiri').count
    bangunrejo_isoman = Warga.objects.filter(padukuhan='Bangunrejo', status='Isolasi Mandiri').count

    wadas_sembuh = Warga.objects.filter(padukuhan='Wadas', status='Sembuh').count
    paten_sembuh = Warga.objects.filter(padukuhan='Paten', status='Sembuh').count
    ngemplak_sembuh = Warga.objects.filter(padukuhan='Ngemplack Caban', status='Sembuh').count
    pangukan_sembuh = Warga.objects.filter(padukuhan='Pangukan', status='Sembuh').count
    beteng_sembuh = Warga.objects.filter(padukuhan='Beteng', status='Sembuh').count
    pisangan_sembuh = Warga.objects.filter(padukuhan='Pisangan', status='Sembuh').count
    dukuh_sembuh = Warga.objects.filter(padukuhan='Dukuh', status='Sembuh').count
    beranlor_sembuh = Warga.objects.filter(padukuhan='Beran Lor', status='Sembuh').count
    josari_sembuh = Warga.objects.filter(padukuhan='Josari', status='Sembuh').count
    drono_sembuh = Warga.objects.filter(padukuhan='Drono', status='Sembuh').count
    berankidul_sembuh = Warga.objects.filter(padukuhan='Beran Kidul', status='Sembuh').count
    kebonagung_sembuh = Warga.objects.filter(padukuhan='Kebonagung', status='Sembuh').count
    jaban_sembuh = Warga.objects.filter(padukuhan='Jaban', status='Sembuh').count
    denggung_sembuh = Warga.objects.filter(padukuhan='Denggung', status='Sembuh').count
    bangunrejo_sembuh = Warga.objects.filter(padukuhan='Bangunrejo', status='Sembuh').count

    wadas_meninggal = Warga.objects.filter(padukuhan='Wadas', status='Meninggal').count
    paten_meninggal = Warga.objects.filter(padukuhan='Paten', status='Meninggal').count
    ngemplak_meninggal = Warga.objects.filter(padukuhan='Ngemplack Caban', status='Meninggal').count
    pangukan_meninggal = Warga.objects.filter(padukuhan='Pangukan', status='Meninggal').count
    beteng_meninggal = Warga.objects.filter(padukuhan='Beteng', status='Meninggal').count
    pisangan_meninggal = Warga.objects.filter(padukuhan='Pisangan', status='Meninggal').count
    dukuh_meninggal = Warga.objects.filter(padukuhan='Dukuh', status='Meninggal').count
    beranlor_meninggal = Warga.objects.filter(padukuhan='Beran Lor', status='Meninggal').count
    josari_meninggal = Warga.objects.filter(padukuhan='Josari', status='Meninggal').count
    drono_meninggal = Warga.objects.filter(padukuhan='Drono', status='Meninggal').count
    berankidul_meninggal = Warga.objects.filter(padukuhan='Beran Kidul', status='Meninggal').count
    kebonagung_meninggal = Warga.objects.filter(padukuhan='Kebonagung', status='Meninggal').count
    jaban_meninggal = Warga.objects.filter(padukuhan='Jaban', status='Meninggal').count
    denggung_meninggal = Warga.objects.filter(padukuhan='Denggung', status='Meninggal').count
    bangunrejo_meninggal = Warga.objects.filter(padukuhan='Bangunrejo', status='Meninggal').count


    padukuhan_dirawat = (wadas_dirawat,
                         paten_dirawat,
                         ngemplak_dirawat,
                         pangukan_dirawat,
                         beteng_dirawat,
                         pisangan_dirawat,
                         dukuh_dirawat,
                         beranlor_dirawat,
                         josari_dirawat,
                         drono_dirawat,
                         berankidul_dirawat,
                         kebonagung_dirawat,
                         jaban_dirawat,
                         denggung_dirawat,
                         bangunrejo_dirawat)

    padukuhan_isoman = (wadas_isoman,
                         paten_isoman,
                         ngemplak_isoman,
                         pangukan_isoman,
                         beteng_isoman,
                         pisangan_isoman,
                         dukuh_isoman,
                         beranlor_isoman,
                         josari_isoman,
                         drono_isoman,
                         berankidul_isoman,
                         kebonagung_isoman,
                         jaban_isoman,
                         denggung_isoman,
                         bangunrejo_isoman)

    padukuhan_sembuh = (wadas_sembuh,
                        paten_sembuh,
                        ngemplak_sembuh,
                        pangukan_sembuh,
                        beteng_sembuh,
                        pisangan_sembuh,
                        dukuh_sembuh,
                        beranlor_sembuh,
                        josari_sembuh,
                        drono_sembuh,
                        berankidul_sembuh,
                        kebonagung_sembuh,
                        jaban_sembuh,
                        denggung_sembuh,
                        bangunrejo_sembuh)

    padukuhan_meninggal = (wadas_meninggal,
                         paten_meninggal,
                         ngemplak_meninggal,
                         pangukan_meninggal,
                         beteng_meninggal,
                         pisangan_meninggal,
                         dukuh_meninggal,
                         beranlor_meninggal,
                         josari_meninggal,
                         drono_meninggal,
                         berankidul_meninggal,
                         kebonagung_meninggal,
                         jaban_meninggal,
                         denggung_meninggal,
                         bangunrejo_meninggal)

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
        'padukuhan': padukuhan_list,
        'padukuhan_dirawat': padukuhan_dirawat,
        'padukuhan_isoman': padukuhan_isoman,
        'padukuhan_sembuh': padukuhan_sembuh,
        'padukuhan_meninggal': padukuhan_meninggal
    }
    return render(request, 'adminDashboard/index.html', context)


@login_required
def database(request):
    warga = Warga.objects.all()
    context = {'warga': warga}

    return render(request, 'adminDashboard/database.html', context)


@login_required
def dataform(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/database/')

    context = {'form': form}

    return render(request, 'adminDashboard/data_form.html', context)


@login_required
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


@login_required
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
