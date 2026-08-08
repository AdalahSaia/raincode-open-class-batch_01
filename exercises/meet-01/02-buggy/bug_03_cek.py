def hitung_diskon(harga, persen_diskon):
    diskon = harga * (persen_diskon / 100)
    harga_akhir = harga - diskon
    # seharusnya ada sesuatu di sini...
    return  harga_akhir 

harga_sepatu = 200000
harga_bayar = hitung_diskon(harga_sepatu, 20)

print("Harga setelah diskon:", harga_bayar)
#output: Harga setelah diskon: 160000.0