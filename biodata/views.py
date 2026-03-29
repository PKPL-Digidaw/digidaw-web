from django.shortcuts import render
from .models import Anggota

MEMBER_EMAILS = [
  #TODO: masukkan email anggota di sini
]

def home(request):
    anggota_list = Anggota.objects.all()

    is_member = (
        request.user.is_authenticated and request.user.email in MEMBER_EMAILS
    )

    return render(request, 'index.html', {
        'anggota_list': anggota_list,
        'is_member': is_member
    })