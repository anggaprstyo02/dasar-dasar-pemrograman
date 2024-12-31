class Animal():
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def info_animal(self):
        print(f"Nama Hewan \t\t : ",self.name,
              "\nMakanan \t\t : ",self.makanan,
              "\nHidup \t\t\t : ",self.hidup,
              "\nBerkembang Biak \t : ",self.berkembang_biak)
        
hewan = Animal("Kucing Garong", "Ikan", "Darat", "Melahirkan")     
hewan.info_animal()

