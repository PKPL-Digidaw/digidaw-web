from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Anggota

MEMBER_EMAILS = [
    'afifah.widhia@ui.ac.id',
    'levina.aurellia@ui.ac.id',
    'dhea.anggrayningsih41@ui.ac.id',
    'nadine.aisyah@ui.ac.id',
    'vidya.pramudita@ui.ac.id'
]

def is_member_user(user):
    return (
        user.is_authenticated and
        user.email and
        user.email.lower().strip() in [e.lower() for e in MEMBER_EMAILS]
    )

def home(request):
    anggota_list = Anggota.objects.all()

    # ambil theme dari session (default kalau belum ada)
    theme = request.session.get('theme', {
        'font': 'Poppins',
        'color': '#ffffff'
    })

    return render(request, 'index.html', {
        'anggota_list': anggota_list,
        'is_member': is_member_user(request.user),
        'theme': theme
    })


def edit(request):
    if not is_member_user(request.user):
        return HttpResponseForbidden("Tidak punya akses")

    theme = request.session.get('theme', {
        'font': 'Poppins',
        'color': '#ffffff'
    })

    if request.method == 'POST':
        font = request.POST.get('font')
        color = request.POST.get('color')

        # simpan ke session
        request.session['theme'] = {
            'font': font,
            'color': color
        }

        return redirect('home')

    return render(request, 'edit.html', {
        'theme': theme
    })