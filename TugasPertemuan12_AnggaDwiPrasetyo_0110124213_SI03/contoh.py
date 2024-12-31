# parent class
class person :
    def __init__(self, nama_depan, nama_belakang):
        self.fnama = nama_depan
        self.lnama = nama_belakang
        
    def masak(self):
        print(f"{self.fnama} sedang memasak opor")
        
arya = person("arya", "purnomo")
arya.masak()        

class Fadhel(person):
        def __init__(self, nama_depan, nama_belakang, koncet):
            super().__init__(nama_depan, nama_belakang)
            self.koncet = koncet
            
        def kuncir(self):
            print(f"{}")    