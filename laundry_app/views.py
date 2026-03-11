from django.shortcuts import render, redirect, get_object_or_404 
from .models import CuciKiloan, CuciSatuan
from .utils.file_io import simpan_struk_ke_media

def manajemen_kasir(request):
    # simpan data
    if request.method == 'POST':
        jenis_layanan = request.POST.get('jenis_layanan')
        nama = request.POST.get('nama_pelanggan')
        alamat_pelanggan = request.POST.get('alamat')
        hp_pelanggan = request.POST.get('no_hp')
        status_bayar = request.POST.get('status_pembayaran')

        if jenis_layanan == 'kiloan':
            berat = float(request.POST.get('berat', 0))
            pesanan = CuciKiloan(
                nama_pelanggan=nama, berat_kg=berat, 
                alamat=alamat_pelanggan, no_hp=hp_pelanggan, status_pembayaran=status_bayar
            )
            pesanan.biaya_tambahan = 2000 
            pesanan.save()
        elif jenis_layanan == 'satuan':
            barang = request.POST.get('nama_barang')
            jumlah_barang = int(request.POST.get('jumlah', 0))
            pesanan = CuciSatuan(
                nama_pelanggan=nama, nama_barang=barang, jumlah=jumlah_barang,
                alamat=alamat_pelanggan, no_hp=hp_pelanggan, status_pembayaran=status_bayar
            )
            pesanan.save()
        return redirect('manajemen_kasir')

    # mengambil data di database
    data_kiloan = CuciKiloan.objects.all()
    data_satuan = CuciSatuan.objects.all()

    # Array gabungan
    semua_pesanan_array = list(data_kiloan) + list(data_satuan)

    # Mencetak log struk ke file fisik setiap kali halaman dimuat
    if len(semua_pesanan_array) > 0:
        simpan_struk_ke_media(semua_pesanan_array)

    # menampilkan data di interface
    context = {
        'kiloan': data_kiloan,
        'satuan': data_satuan
    }
    
    return render(request, 'index.html', context)


# Fungsi untuk tombol ubah status di tabel
def update_status(request, tipe, id):
    if request.method == "POST":
        if tipe == "kiloan":
            obj = get_object_or_404(CuciKiloan, id=id)
        else:
            obj = get_object_or_404(CuciSatuan, id=id)

        # mengubah status 
        if 'ubah_cucian' in request.POST:
            obj.status_cucian = "Selesai" if obj.status_cucian == "Proses" else "Proses"
        elif 'ubah_bayar' in request.POST:
            obj.status_pembayaran = "Lunas" if obj.status_pembayaran == "Belum Lunas" else "Belum Lunas"
        obj.save()
        
    return redirect('manajemen_kasir')

# Fungsi khusus untuk menghapus data pesanan
def hapus_pesanan(request, tipe, id):
    if request.method == "POST":
        if tipe == "kiloan":
            obj = get_object_or_404(CuciKiloan, id=id)
        else:
            obj = get_object_or_404(CuciSatuan, id=id)
        obj.delete()
        
    return redirect('manajemen_kasir')