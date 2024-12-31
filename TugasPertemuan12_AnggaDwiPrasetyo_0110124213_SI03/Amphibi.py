from Animal import Animal

# setiap class child itu memiliki 2 method dan properti
class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, alat_bernafas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.alat_bernafas = alat_bernafas
        
    def info_Amphibi(self):
        super().info_animal(),
        print("Jenis air \t\t : ", self.jenis_air,
              "\nBernapas \t\t : ", self.alat_bernafas)   
        
amphibi = Amphibi("katak Bhizer", "Berudu", "Air", "Bertelur", "Air Rawa", "Kulit")
amphibi.info_Amphibi()