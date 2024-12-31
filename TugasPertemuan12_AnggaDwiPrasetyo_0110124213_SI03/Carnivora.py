from Animal import Animal

class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, alat_bernafas, ukuran_badan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.alat_bernafas = alat_bernafas
        self.ukuran_badan = ukuran_badan
        
    def info_Carnivora(self):
        super().info_animal(),
        print("Bernapas \t\t : ", self.alat_bernafas,
              "\nUkuran Badan \t\t : ", self.ukuran_badan,)
        
carnivora = Carnivora("Macan Tutul", "Daging", "Daratan", "Melahirkan", "Paru-Paru", "Lumayan Gede")
carnivora.info_Carnivora()