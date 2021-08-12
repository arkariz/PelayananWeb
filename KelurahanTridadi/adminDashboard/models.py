from django.db import models
from datetime import date, datetime


# Create your models here.
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

    nik = models.IntegerField()
    nama = models.CharField(max_length=40)
    jenis_kelamin = models.CharField(choices=GENDER_CHOICES, max_length=10)
    tanggal_lahir = models.DateField()
    usia = models.IntegerField(null=True)
    no_kontak = models.IntegerField()

    padukuhan = models.CharField(choices=DUKUH_CHOICES, max_length=20)
    rt = models.IntegerField()
    rw = models.IntegerField()
    alamat = models.TextField(max_length=100)

    tanggal_input = models.DateField(default=date.today)
    waktu_input = models.TimeField(default=datetime.now().time())
    status = models.CharField(choices=STATUS_CHOICES, default='Konfirmasi', max_length=25)

    faskes_awal = models.CharField(max_length=25, default='Puskesmas Sleman')
    Rujukan = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama
