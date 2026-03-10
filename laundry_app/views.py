from django.shortcuts import render, redirect
from .models import CuciKiloan, CuciSatuan
from .utils.file_io import simpan_struk_ke_media

def manajemen_kasir(request):
    """ 
    Fungsi utama untuk menangani input dari tampilan (Syarat 3c)
    serta melakukan operasi CRUD (Create & Read).
    """
    # Mengambil data dari database & memasukkannya ke dalam Array/List (Syarat 3f)
    data_kiloan = list(CuciKiloan.objects.all())
    data_satuan = list(CuciSatuan.objects.all())
    
    # Array gabungan
    semua_pesanan_array = data_kiloan + data_satuan

    # PERCABANGAN if..elif..else (Syarat 3d)
    if request.method == "POST":
        jenis_layanan = request.POST.get('jenis_layanan')
        nama = request.POST.get('nama_pelanggan')
        
        # CREATE: Menyimpan data baru ke Database
        if jenis_layanan == "kiloan":
            berat = float(request.POST.get('berat', 0))
            # Instansiasi objek dan simpan (CRUD - Create)
            pesanan_baru = CuciKiloan(nama_pelanggan=nama, berat_kg=berat)
            pesanan_baru.biaya_tambahan = 2000 # Menggunakan properti setter
            pesanan_baru.save()
            
        elif jenis_layanan == "satuan":
            barang = request.POST.get('nama_barang')
            jumlah = int(request.POST.get('jumlah', 0))
            # Instansiasi objek dan simpan (CRUD - Create)
            pesanan_baru = CuciSatuan(nama_pelanggan=nama, nama_barang=barang, jumlah=jumlah)
            pesanan_baru.save()
            
        return redirect('manajemen_kasir') # Refresh halaman untuk menghindari submit ganda
    
    # Mencetak log struk ke file fisik setiap kali halaman dimuat
    if len(semua_pesanan_array) > 0:
        simpan_struk_ke_media(semua_pesanan_array)

    # Konteks data yang akan dikirim ke antarmuka HTML
    context = {
        'kiloan': data_kiloan,
        'satuan': data_satuan
    }
    
    return render(request, 'index.html', context)
