#exaclass.py #pendeklarasian class

class Orang:
    #variabel(atribut = variabel didalam class)
    nama = ""
    nama_mahasiswa = "Angga"
    nama_Supir = "Yazid"
    nama_Dokter = "Naufal"
    umur = 0

    #fungsi(method = fungsi didalam class)
    def ngomong(self):
        print("Halo, saya adalah orang")
    
#membuat objek
supir = Orang()
supir.nama = "Budi"
supir.nama_Supir = ""
supir.umur = 30
print(supir.nama)
print(supir.umur)
print(supir.nama_Supir)
supir.ngomong()

dokter = Orang()
dokter.nama = "Angga"
dokter.nama_Dokter = ""
dokter.sertifikat = "0110124213"
print(dokter.sertifikat) 
print(dokter.nama)
print(dokter.nama_Dokter)
dokter.ngomong()

mahasiswa = Orang()
mahasiswa.kampus = "Nurul Fikri"
mahasiswa.prodi = "SI"
mahasiswa.nama_mahasiswa
print(mahasiswa.kampus)
print(mahasiswa.prodi)
print(supir.nama_mahasiswa)
mahasiswa.ngomong()

class Mobil:
    bensin = ""
    merek = ""

    def maju(self):
        print("Mobil dia berjalan")

dia = Mobil()
dia.merek = "Toyota"
dia.bensin = "Pertamax Turbo"
print(dia.merek)
print(dia.bensin)
dia.maju()



class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def ngomong(self, nama):
        print(f"Saya bernama {self.nama}")

supir = Manusia("Angga", 20)
print(supir.nama)
print(supir.umur)
