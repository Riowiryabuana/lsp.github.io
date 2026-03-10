// 1. Logika untuk mengganti menu (Menyembunyikan yang tidak diklik)
function gantiMenu(idHalaman) {
    // Sembunyikan semua section
    document.getElementById("halaman-dashboard").style.display = "none";
    document.getElementById("halaman-tambah").style.display = "none";
    document.getElementById("halaman-antrean").style.display = "none";

    // Tampilkan hanya section yang dipilih
    document.getElementById(idHalaman).style.display = "block";

    // Ubah judul utama sesuai menu
    var judul = document.getElementById("judul-halaman");
    if (idHalaman === 'halaman-dashboard') judul.innerText = "Dashboard Admin";
    if (idHalaman === 'halaman-tambah') judul.innerText = "Tambah Pesanan Baru";
    if (idHalaman === 'halaman-antrean') judul.innerText = "Manajemen Antrean";
}

// 2. Logika bawaan untuk mengubah tipe form (Kiloan / Satuan)
function ubahForm() {
    var jenis = document.getElementById("jenis_layanan").value;
    if (jenis === "kiloan") {
        document.getElementById("form_kiloan").style.display = "block";
        document.getElementById("form_satuan").style.display = "none";
    } else {
        document.getElementById("form_kiloan").style.display = "none";
        document.getElementById("form_satuan").style.display = "block";
    }
}

// 3. Logika untuk menggambar Grafik (Chart.js)
// Kode ini akan otomatis berjalan saat halaman web selesai dimuat
document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('grafikKeuangan').getContext('2d');
    
    var myChart = new Chart(ctx, {
        type: 'bar', // Tipe diagram batang
        data: {
            labels: ['Minggu 1', 'Minggu 2', 'Minggu 3', 'Minggu 4'],
            datasets: [
                {
                    label: 'Penjualan (Rp)',
                    data: [1500000, 2300000, 1800000, 3200000], // Data simulasi
                    backgroundColor: 'rgba(16, 185, 129, 0.7)', // Hijau untuk untung
                    borderColor: 'rgba(16, 185, 129, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Pengeluaran (Rp)',
                    data: [800000, 1200000, 900000, 1500000], // Data simulasi (deterjen, listrik, dll)
                    backgroundColor: 'rgba(239, 68, 68, 0.7)', // Merah untuk rugi/keluar
                    borderColor: 'rgba(239, 68, 68, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});