from django.db import models

# 1. INTERFACE
class KalkulasiLayanan:
    """ Interface untuk standarisasi kalkulasi layanan (Syarat 3h) """
    def hitung_total_harga(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini!")

# 2. SUPERCLASS
class PesananUtama(models.Model, KalkulasiLayanan):
    """ Superclass entitas pesanan dengan Eksternal Library ORM Django (Syarat 3j & 3k) """
    nama_pelanggan = models.CharField(max_length=100)
    tanggal_masuk = models.DateTimeField(auto_now_add=True)
    
    # ENCAPSULATION
    _biaya_tambahan = models.FloatField(default=0.0)

    # PROPERTIES
    @property
    def biaya_tambahan(self):
        return self._biaya_tambahan

    @biaya_tambahan.setter
    def biaya_tambahan(self, nilai):
        if nilai < 0:
            raise ValueError("Biaya tambahan tidak boleh negatif!")
        self._biaya_tambahan = nilai

    # OVERLOADING
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

# 3. SUBCLASS 1
class CuciKiloan(PesananUtama):
    berat_kg = models.FloatField()
    harga_per_kg = models.FloatField(default=8000.0)

    # POLYMORPHISM
    def hitung_total_harga(self):
        return (self.berat_kg * self.harga_per_kg) + self.biaya_tambahan

# 4. SUBCLASS 2
class CuciSatuan(PesananUtama):
    nama_barang = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    harga_per_item = models.FloatField(default=15000.0)

    # POLYMORPHISM
    def hitung_total_harga(self):
        return (self.jumlah * self.harga_per_item) + self.biaya_tambahan