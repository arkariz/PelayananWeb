# Generated by Django 3.2.6 on 2021-08-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminDashboard', '0003_alter_warga_jenis_kelamin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warga',
            name='jenis_kelamin',
            field=models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=10),
        ),
    ]