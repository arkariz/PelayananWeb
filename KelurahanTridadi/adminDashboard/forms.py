from django import forms
from .models import Warga


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PostForm(forms.ModelForm):
    Rujukan = forms.CharField(required=False)

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
            'tanggal_input',
            'status',
            'faskes_awal',
            'Rujukan'
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
            'tanggal_input': DateInput(attrs={'class': "form-control"}),
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
