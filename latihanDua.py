class Kendaraan:
    def __init__(self, kecepatan_maksimum, jenis):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print(f"Jenis kendaraan: {self.jenis}")

    def bergerak(self):
        print(f"{self.jenis} sedang bergerak")

    
class Mobil(Kendaraan):
    def __init__(self, merk, jumlah_pintu, kecepatan_maksimum):
        super().__init__(kecepatan_maksimum, jenis = "Mobil")
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        print(f"Jenis kendaraan : {self.jenis}")
        print(f"Merk {self.jenis} : {self.merk}")

    def bunyikan_klakson(self):
        print("Beep Beep")
    
class mobilSport(Mobil):
    __tenaga_kuda = "belum diinputkan"
    __harga = "sedang didiskusikan"

    def __init__(self, merk, jumlah_pintu, kecepatan_maksimum):
        super().__init__(merk, jumlah_pintu, kecepatan_maksimum)

    def get_tenaga_kuda(self):
        print(f"Tenaga kuda : {self.__tenaga_kuda}")

    def set_tenaga_kuda(self, new_tenaga_kuda):
        self.__tenaga_kuda = new_tenaga_kuda

    def get_harga(self):
        print(f"harga : {self.__harga}")

    def set_harga(self, new_harga):
        self.__harga = new_harga

    def info_mobil_sport(self):
        print(f"Jenis mobil : {self.merk}")
        print(f"Jumlah pintu : {self.jumlah_pintu}")
        self.get_tenaga_kuda()
        print(f"kecepatan maksimum : {self.kecepatan_maksimum}")
        self.get_harga()

    def mode_balap(self):
        print("dalam mode balap")


car1 = Mobil("BMW", 4, 350)
car1.info_mobil()
car1.bunyikan_klakson()
print("\n")

car2 = Kendaraan(250, "Mobil")
car2.bergerak()
car2.info_kendaraan()
print("\n")

sport_car = mobilSport("Lamborghini", 2, 400)
sport_car.info_mobil_sport()
sport_car.set_tenaga_kuda(100)
sport_car.set_harga("3 Miliyar")
print("\n")

sport_car.info_mobil_sport()
sport_car.mode_balap()