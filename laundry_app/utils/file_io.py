import os

# FUNGSI 
def simpan_struk_ke_media(data_pesanan_array):
    """
    Fungsi menyimpan data ke media penyimpan komputer. (Syarat 3g)
    Menerima parameter berupa Array/List berisi objek pesanan.
    """
    filepath = "log_transaksi_cleandong.txt"
    
    # Context manager untuk operasi File I/O
    with open(filepath, 'a') as file:
        file.write("\n=== STRUK CLEAN DONG LAUNDRY ===\n")
        
        # PENGULANGAN for
        for pesanan in data_pesanan_array:
            # Memanggil fungsi polimorfisme untuk mencetak total
            file.write(f"Pelanggan: {pesanan.nama_pelanggan} | Total Bayar: Rp{pesanan.hitung_total_harga()}\n")
            
        file.write("==================================\n")
