print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32 #mengkonversi suhu dari celcius ke fahrenheit
    return fahrenheit #mengembalikan nilai fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
#cetak 0 celcius ke 32 fahrenheit
suhu_fahrenheit1 = celcius_ke_fahrenheit(suhu_celcius1)
print('Suhu Celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1, 'f')
#cetak 100 celcius ke 212 fahrenheit
suhu_fahrenheit2 = celcius_ke_fahrenheit(suhu_celcius2)
print('Suhu Celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2, 'f')
    
print('======================================================')
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 #menentukan bilangan ganjil atau genap
    return hitung #mengembalikan nilai hitung

angka = 4
hasil = genap_ganjil(angka)
print(f"Bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"Bilangan {angka2} bernilai {hasil2}")

print('======================================================')
print('## Nomor 3 ##')
def cek_kelulusan(nilai):
    if nilai > 60:
        return 'Lulus'
    else:
        return 'Gagal'

nilai_kamu = 60
Status = cek_kelulusan(nilai_kamu)
print(f"Nilai: {nilai_kamu}, Dan kamu dinyatakan: {Status}")

nilai_kamu = 90
Status = cek_kelulusan(nilai_kamu)
print(f"Nilai: {nilai_kamu}, Dan kamu dinyatakan: {Status}")

print('======================================================')
print('## Nomor 4 ##')

def bilanganGanjil(nilai): #nilai = bilangan yang ingin dicari
    return[str(i) for i in range(1,nilai,2)]
print(bilanganGanjil(20)) #(20) nilai yang telah di masukkan