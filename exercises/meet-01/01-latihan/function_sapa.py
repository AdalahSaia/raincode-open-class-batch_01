#===========Bagian 1===========
def sapa_formal(nama):
    return "Selamat datang, " + nama + "!"

pesan = sapa_formal("Budi")
print(pesan)

#otput: Selamat datang, Budi! ✅

#===========Bagian 2===========

def sapa(nama):
    return "Halo, " + nama + "!" + " Apa kabar?"
 
pesan = sapa("Pipit") 
print(pesan)

pesan = sapa("Afifah")
print(pesan)

pesan = sapa("Jarwo")
print(pesan)

#============Bonus=============
def sapa(nama,kota):
    return "Halo, " + nama + " dari " + kota + "!"

pesan = sapa("Pipit", "Bandung")
print(pesan)