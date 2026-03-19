from django.shortcuts import render
from .models import Anggota

def home(request):
    anggota_list = Anggota.objects.all()

    return render(request, 'index.html', {'anggota_list': anggota_list})