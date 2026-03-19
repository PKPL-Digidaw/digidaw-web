from django.db import models

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='foto_anggota/', blank=True, null=True)

    def __str__(self):
        return self.nama