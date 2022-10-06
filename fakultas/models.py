from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIPDosen= models.CharField(max_length=30)
    NAMA = models.CharField(max_length=30)
    TTL = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=30)
    FAKULTAS = models.CharField(max_length=30)
    PRODI = models.CharField(max_length=30)
    ALAMAT = models.CharField(max_length=30)
    PHOTO = models.CharField(max_length=30)

    def __str__(self):
        return self.NIPDosen

class Tendik(models.Model):
    NIPTendik= models.CharField(max_length=30)
    NAMA = models.CharField(max_length=30)
    TTL = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=30)
    FAKULTAS = models.CharField(max_length=30)
    PRODI = models.CharField(max_length=30)
    ALAMAT = models.CharField(max_length=30)
    PHOTO = models.CharField(max_length=30)

    def __str__(self):
        return self.NIPTendik

class Mahasiswa(models.Model):
    NIK= models.CharField(max_length=30)
    NAMA = models.CharField(max_length=30)
    TTL = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=30)
    FAKULTAS = models.CharField(max_length=30)
    PRODI = models.CharField(max_length=30)
    ALAMAT = models.CharField(max_length=30)
    PHOTO = models.CharField(max_length=30)

    def __str__(self):
        return self.NIK