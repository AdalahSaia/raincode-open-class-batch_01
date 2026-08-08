#==========luas persegi==========
def luas_persegi(sisi):
    return sisi * sisi

print(luas_persegi(4))
print(luas_persegi(7))
print(luas_persegi(10))

#output:
#16
#49
#100

#==========keliling persegi==========
def keliling_persegi (sisi):
    return 4 * sisi

print(keliling_persegi(5))
print(keliling_persegi(3))

#output:
#20✅
#12✅

#==========gabungkan keduanya==========
sisi = 6
luas = luas_persegi(sisi)
keliling = keliling_persegi(sisi)

print(f"Persegi dengan sisi {sisi}: luas = {luas},keliling = {keliling}")
#output: Persegi dengan sisi 6: luas = 36,keliling = 24