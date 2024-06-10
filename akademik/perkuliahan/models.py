from django.db import models

# Create your models here.
class Jurusan(models.Model):
    kodejurusan = models.CharField(max_length=50, null=False, blank=False, verbose_name='Kode Program Studi')
    namajurusan = models.CharField(max_length=150, null=False, blank=False, verbose_name='Program')
    level =(
        ('S1','STRATA-1'),
        ('S2','STRATA-2'),
        ('S3','STRATA-3'),
        ('D3','DIPLOMA-3'),
        ('D4','DIPLOMA-4'),
    )
    jenjang = models.CharField(max_length=150, null=True, blank=True, verbose_name='Jenjang', choices=level)

    def __str__(self):
        return self.namajurusan

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nim')
    nama = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nama Lengkap')
    jeniskelamin_choices = (
        ('L', 'LAKI-LAKI'),
        ('P', 'PEREMPUAN'),
    )
    jeniskelamin = models.CharField(max_length=50, verbose_name='Jenis Kelamin', choices=jeniskelamin_choices)
    email = models.EmailField(max_length=150, null=True, blank=True, verbose_name='Email', help_text='contoh: admin@gmail.com')
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

class Matakuliah(models.Model):
    kodemk = models.CharField(max_length=100, null=False, blank=False, verbose_name='Kode Mata Kuliah')
    namamk = models.CharField(max_length=150, null=False, blank=False, verbose_name='Nama Mata Kuliah')
    semester = models.CharField(max_length=50, verbose_name='Semester')
    sks = models.IntegerField(verbose_name='SKS')
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)

    def __str__(self):
        return self.namamk
