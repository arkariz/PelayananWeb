from django.db import models
from datetime import date


class Warga(models.Model):
    GENDER_CHOICES = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan')
    )

    DUKUH_CHOICES = (
        ('Wadas', 'Wadas'),
        ('Paten', 'Paten'),
        ('Ngemplak Caban', 'Ngemplak Caban'),
        ('Pangukan', 'Pangukan'),
        ('Beteng', 'Beteng'),
        ('Pisangan', 'Pisangan'),
        ('Dukuh', 'Dukuh'),
        ('Beran Lor', 'Beran Lor'),
        ('Josari', 'Josari'),
        ('Drono', 'Drono'),
        ('Beran Kidul', 'Beran Kidul'),
        ('Kebonagung', 'Kebonagung'),
        ('Jaban', 'Jaban'),
        ('Denggung', 'Denggung'),
        ('Bangunrejo', 'Bangunrejo')
    )

    STATUS_CHOICES = (
        ('Konfirmasi', 'Konfirmasi'),
        ('Isolasi Mandiri', 'Isolasi Mandiri'),
        ('Dirawat', 'Dirawat'),
        ('Sembuh', 'Sembuh'),
        ('Meninggal', 'Meninggal')
    )

    nik = models.CharField(max_length=40)
    nama = models.CharField(max_length=40)
    jenis_kelamin = models.CharField(choices=GENDER_CHOICES, max_length=10)
    tanggal_lahir = models.DateField()
    usia = models.IntegerField(null=True)
    no_kontak = models.CharField(max_length=40)

    padukuhan = models.CharField(choices=DUKUH_CHOICES, max_length=20)
    rt = models.IntegerField()
    rw = models.IntegerField()
    alamat = models.TextField(max_length=100)

    tanggal_penanganan = models.DateField(default=date.today)
    tanggal_input = models.DateField(default=date.today)
    waktu_input = models.TimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='Konfirmasi', max_length=25)

    faskes_awal = models.CharField(max_length=25, default='Puskesmas Sleman')
    Rujukan = models.CharField(max_length=50, blank=True, default=" ")
    last_update = models.DateField(auto_now=True)
    last_update_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.nama


class Penanganan(models.Model):

    STATUS_CHOICES = (
        ('Konfirmasi', 'Konfirmasi'),
        ('Isolasi Mandiri', 'Isolasi Mandiri'),
        ('Dirawat', 'Dirawat'),
        ('Sembuh', 'Sembuh'),
        ('Meninggal', 'Meninggal')
    )

    warga = models.ForeignKey(Warga, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default='Konfirmasi', max_length=25)
    tanggal_penanganan = models.DateField(default=date.today)
    Rujukan = models.CharField(max_length=50, blank=True, default=" ")


class Vaksinasi(models.Model):
    GENDER_CHOICES = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan')
    )

    VAKSIN_CHOICES = (
        ('SINOVAC', 'SINOVAC'),
        ('BIO FARMA', 'BIO FARMA'),
        ('AstraZeneca', 'AstraZeneca'),
        ('SINOPHARM', 'SINOPHARM'),
        ('MODERNA', 'MODERNA'),
        ('PFIZER', 'PFIZER')
    )

    DUKUH_CHOICES = (
        ('Wadas', 'Wadas'),
        ('Paten', 'Paten'),
        ('Ngemplak Caban', 'Ngemplak Caban'),
        ('Pangukan', 'Pangukan'),
        ('Beteng', 'Beteng'),
        ('Pisangan', 'Pisangan'),
        ('Dukuh', 'Dukuh'),
        ('Beran Lor', 'Beran Lor'),
        ('Josari', 'Josari'),
        ('Drono', 'Drono'),
        ('Beran Kidul', 'Beran Kidul'),
        ('Kebonagung', 'Kebonagung'),
        ('Jaban', 'Jaban'),
        ('Denggung', 'Denggung'),
        ('Bangunrejo', 'Bangunrejo')
    )

    nik = models.CharField(max_length=40)
    nama = models.CharField(max_length=40)
    jenis_kelamin = models.CharField(choices=GENDER_CHOICES, max_length=10)
    tanggal_lahir = models.DateField()
    usia = models.IntegerField(null=True)
    no_kontak = models.CharField(max_length=40)

    padukuhan = models.CharField(choices=DUKUH_CHOICES, max_length=20)
    rt = models.IntegerField()
    rw = models.IntegerField()
    alamat = models.TextField(max_length=100)

    jenis_vaksin = models.CharField(choices= VAKSIN_CHOICES, max_length=25)
    tanggal_vaksin_pertama = models.DateField(default=date.today)
    tanggal_vaksin_kedua = models.DateField(default=" ", blank=True, null=True)
    faskes = models.CharField(max_length=25, default='Puskesmas Sleman')

    last_update = models.DateField(auto_now=True)
    last_update_time = models.TimeField(auto_now=True)
    tanggal_input = models.DateField(auto_now_add=True)