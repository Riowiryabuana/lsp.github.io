from django.db import models
# Hapus baris 'from abc import ABC, abstractmethod'

# 1. INTERFACE (Tanpa modul ABC agar tidak bentrok dengan Django ORM)
class KalkulasiLayanan:
    """ Interface untuk standarisasi kalkulasi layanan (Syarat 3h) """
    def hitung_total_harga(self):
        # Ini memaksa subclass untuk membuat metode ini, persis seperti fungsi Interface
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini!")

# 2. SUPERCLASS (Mewarisi Model Database Django dan Interface KalkulasiLayanan)
class PesananUtama(models.Model, KalkulasiLayanan):
    """ Superclass entitas pesanan dengan Eksternal Library ORM Django (Syarat 3j & 3k) """
    nama_pelanggan = models.CharField(max_length=100)
    tanggal_masuk = models.DateTimeField(auto_now_add=True)
    
    # ENCAPSULATION / HAK AKSES (Private attribute) (Syarat 3h)
    _biaya_tambahan = models.FloatField(default=0.0)

    # PROPERTIES (Getter & Setter) (Syarat 3h)
    @property
    def biaya_tambahan(self):
        return self._biaya_tambahan

    @biaya_tambahan.setter
    def biaya_tambahan(self, nilai):
        if nilai < 0:
            raise ValueError("Biaya tambahan tidak boleh negatif!")
        self._biaya_tambahan = nilai

    # OVERLOADING (Simulasi via default arguments di Python) (Syarat 3h)
    def terapkan_diskon(self, persen=0, potongan_langsung=0):
        """ Menghitung diskon dengan cara yang berbeda tergantung parameter """
        total = self.hitung_total_harga()
        if persen > 0:
            return total * (1 - (persen / 100))
        elif potongan_langsung > 0:
            return total - potongan_langsung
        return total

    def hitung_total_harga(self):
        """ Metode default, akan di-override oleh Subclass """
        return 0.0

# 3. SUBCLASS 1 (Inheritance)
class CuciKiloan(PesananUtama):
    berat_kg = models.FloatField()
    harga_per_kg = models.FloatField(default=8000.0)

    # POLYMORPHISM (Override fungsi dari superclass)
    def hitung_total_harga(self):
        return (self.berat_kg * self.harga_per_kg) + self.biaya_tambahan

# 4. SUBCLASS 2 (Inheritance)
class CuciSatuan(PesananUtama):
    nama_barang = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    harga_per_item = models.FloatField(default=15000.0)

    # POLYMORPHISM (Override fungsi dengan kalkulasi berbeda)
    def hitung_total_harga(self):
        return (self.jumlah * self.harga_per_item) + self.biaya_tambahan