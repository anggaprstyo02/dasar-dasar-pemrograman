from Animal import Animal


class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ukuran_tubuh, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

        
    def info_Mamalia(self):
        super().info_animal(),
        print("Ukuran Tubuh \t\t : ", self.ukuran_tubuh,
              "\nBernapas \t\t : ", self.jenis_kulit)   
        
Mamalia = Mamalia("Lumba-Lumba", "Ikan", "Air", "Melahirkan", "Sedang", "Lembut")
Mamalia.info_Mamalia()