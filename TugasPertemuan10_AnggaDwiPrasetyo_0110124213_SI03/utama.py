from aritmatika import *

def aritmatika():
    print('Pilih operasi aritmatika yang ingin dilakukan:')
    print('1.Penambahan')
    print('2.Pengurangan')
    print('3.Perkalian')
    print('4.Pembagian')
    print('5.Pangkat')
    pilihan = int(input('Masukkan nomor operasi aritmatika yang dipilih: '))

    if pilihan == 1:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', tambah(a,b))
    elif pilihan == 2:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', kurang(a,b))
    elif pilihan == 3:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', kali(a,b))
    elif pilihan == 4:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', bagi(a,b))
    elif pilihan == 5:
        a = float(input('Masukkan angka pertama:'))
        b = float(input('Masukkan angka kedua:'))
        print('Hasil nya adalah:', pangkat(a,b))
    else:
        print('pilihan tidak valid')

from bangundatar import *

def luas_datar():
    print('Pilih Operasi Bangun Datar yang ingin dilakukan:')
    print('1.Persegi')
    print('2.Persegi Panjang')
    print('3.Segitiga')
    print('4.Lingkaran')
    print('5.Trapesium')
    pilihan = int(input('Masukkan nomor operasi Bangun Datar yang dipilih: '))

    if pilihan == 1:
        a = float(input('Masukkan Nilai Sisi Awal: '))
        print("Hasil Luas nya adalah: ", persegi(a))
    elif pilihan == 2:
        a = float(input('Masukkan Panjang:'))
        b = float(input('Masukkan Lebar:'))
        print('Hasil Luas nya adalah: ', persegi_panjang(a,b))
    elif pilihan == 3:
        a = float(input('Masukkan Alas:'))
        b = float(input('Masukkan Tinggi:'))
        print('Hasil Luas nya adalah: ', segitiga(a,b))
    elif pilihan == 4:
        a = float(input('Masukkan Jari-Jari:'))
        print('Hasil Luas nya adalah: ', lingkaran(a))
    elif pilihan == 5:
        a = float(input('Masukkan Sisi 1:'))
        b = float(input('Masukkan Sisi 2:'))
        print('Hasil Luas nya adalah: ', jajar_genjang(a,b))
    else:
        print('Pilihan Tidak Valid.')

from bangunruang import *

def bangun_ruang():
    print('Pilih operasi Luas Bangun Ruang yang ingin dilakukan:')
    print('1.Kubus')
    print('2.Balok')
    print('3.Tabung')
    print('4.Prisma')
    print('5.Limas')
    pilihan = int(input('Masukkan nomor operasi Bangun Datar yang dipilih: '))

    if pilihan == 1:
        a = float(input('Masukkan Sisi:'))
        print('Hasil Luas nya adalah: ', kubus(a))
    elif pilihan == 2:
        a = float(input('Masukkan Panjang:'))
        b = float(input('Masukkan Lebar:'))
        c = float(input('Masukkan Tinggi:'))
        print('Hasil Luas nya adalah: ', balok(a,b,c))
    elif pilihan == 3:
        a = float(input('Masukkan Jari-Jari:'))
        b = float(input('Masukkan Tinggi:'))
        print('Hasil Luas nya adalah: ', tabung(a,b))
    elif pilihan == 4:
        a = float(input('Masukkan Jari-Jari:'))
        b = float(input('Masukkan Tinggi Alas:'))
        c = float(input('Masukkan Tinggi Prisma:'))
        print('Hasil Luas nya adalah: ', prisma(a,b,c))
    elif pilihan == 5:
        a = float(input('Masukkan Alas:'))
        b = float(input('Masukkan Tinggi:'))
        c = float(input('Masukkan Luas Sisi Tegak:'))
        print('Hasil Luas nya adalah: ', limas(a,b,c))
    else:
        print('Pilihan Tidak Valid.')

def Menu():
    print('Silahkan pilih Operasi Bilangan berikut ini: ')
    print('1.Aritmatika')
    print('2.Luas Bangun Datar')
    print('3.Luas Bangun Ruang')
    print('4.Keluar dari program')

def utama():
    while True:
        Menu()
        inputan=input('Silahkan masukkan operasi yang ingin dijalankan (1,2,3, dan 4 jika ingin keluar):')
        if inputan == '1':
            aritmatika()
        elif inputan == '2':
            luas_datar()
        elif inputan == '3':
            bangun_ruang()
        elif inputan == '4':
            print('Program telah berhenti, Terima Kasih.')
            break
        else:
            print('Silahkan coba lagi.')

if __name__ == "__main__":
    utama()