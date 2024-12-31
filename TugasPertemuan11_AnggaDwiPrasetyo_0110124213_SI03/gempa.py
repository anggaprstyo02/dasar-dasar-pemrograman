class Gempa:
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi
        

    def dampak(self):
        print(f"Ada gempa woy di {self.lokasi}")
        print(f"Skala dari gempa disono adalah {self.skala}", "Sr")
        if self.skala < 2:
            print("Dampak ga berasa")
        elif self.skala > 2 and self.skala < 4:
            print("Dampak gempa bangunan retak-retak")
        elif self.skala > 4 and self.skala < 6:
            print("Dampak gempa bangunan roboh")
        elif self.skala > 6:
            print("Dampak gempa bangunan roboh, dan berpotensi tsunami")
        else :
            ("Sistem tidak bisa mendeteksi skala gempa")


gempa1 = Gempa(1.2, "Banten")
gempa1.dampak()
print("=====================")
gempa2 = Gempa(6.1, "Palu")
gempa2.dampak()
print("=====================")
gempa3 = Gempa(5.6, "Cianjur")
gempa3.dampak()
print("=====================")
gempa4 = Gempa(3.3, "Jayapura")
gempa4.dampak()
print("=====================")
gempa5 = Gempa(4.4, "Garut")
gempa5.dampak()


# gempa1 = Gempa(6.1, "Jawa Barat")
# gempa1.dampak()
# print("===============================") 
# gempa1 = Gempa(6.1, "Jawa Barat")
# gempa1.dampak()
# print("===============================") 
# gempa1 = Gempa(6.1, "Jawa Barat")
# gempa1.dampak()
# print("===============================") 
# gempa1 = Gempa(6.1, "Jawa Barat")
# gempa1.dampak()
# print("===============================") 

 