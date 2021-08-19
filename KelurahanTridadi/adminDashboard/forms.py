from django import forms
from .models import Warga


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):

    class Meta:
        model = Warga
        fields = (
            'nik',
            'nama',
            'jenis_kelamin',
            'tanggal_lahir',
            'usia',
            'no_kontak',
            'padukuhan',
            'rt',
            'rw',
            'alamat',
            'tanggal_penanganan',
            'status',
            'faskes_awal',
        )

        widgets = {
            'nik': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'nama': forms.TextInput(
                attrs={'class': 'form-control', 'type': "text", 'required': ""}),
            'jenis_kelamin': forms.Select(
                attrs={'class': "form-control"}),
            'tanggal_lahir': DateInput(attrs={'class': "form-control"}),
            'usia': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'tanggal_penanganan': forms.DateInput(attrs={'class': "form-control", 'type': "Date"}),
            'no_kontak': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'padukuhan': forms.Select(
                attrs={'class': "form-control", 'type': "text", 'required': ""}),
            'rt': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'rw': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'alamat': forms.Textarea(
                attrs={'class': 'form-control', 'type': "text", 'required': ""}),
            'status': forms.Select(
                attrs={'class': "form-control", 'type': "text", 'required': ""}),
            'faskes_awal': forms.TextInput(
                attrs={'class': 'form-control', 'type': "text", 'required': ""}),
        }


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Warga
        fields = (
            'nik',
            'nama',
            'jenis_kelamin',
            'tanggal_lahir',
            'usia',
            'no_kontak',
            'padukuhan',
            'rt',
            'rw',
            'alamat',
            'faskes_awal',
        )

        widgets = {
            'nik': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'nama': forms.TextInput(
                attrs={'class': 'form-control', 'type': "text", 'required': ""}),
            'jenis_kelamin': forms.Select(
                attrs={'class': "form-control"}),
            'tanggal_lahir': DateInput(attrs={'class': "form-control"}),
            'usia': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'no_kontak': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'padukuhan': forms.Select(
                attrs={'class': "form-control", 'type': "text", 'required': ""}),
            'rt': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'rw': forms.NumberInput(
                attrs={'class': 'form-control', 'type': "number", 'required': ""}),
            'alamat': forms.Textarea(
                attrs={'class': 'form-control', 'type': "text", 'required': ""}),
            'faskes_awal': forms.TextInput(
                attrs={'class': 'form-control', 'type': "text", 'required': ""}),
        }


class PenangananForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = (
            'status',
            'Rujukan',
            'tanggal_penanganan'
        )

        widgets = {
            'status': forms.Select(
                attrs={'class': "form-control", 'id': "select_status", 'type': "text", 'required': ""}),
            'Rujukan': forms.TextInput(
                attrs={'class': 'form-control no-validate', 'type': "text"}),
            'tanggal_penanganan': forms.DateInput(attrs={'class': "form-control", 'type': "Date"})
        }