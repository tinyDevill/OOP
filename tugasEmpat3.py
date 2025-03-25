from abc import ABC
class Animal(ABC):
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, species = "Anjing")
        self.name = name
        self.age = age
        self.__sound = "Guk guk"

    def make_sound(self):
        return self.__sound
    
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, species = "Kucing")
        self.name = name
        self.age = age
        self.__sound = "Meow meow"

    def make_sound(self):
        return self.__sound

def add(cats_or_dogs):
    name = input(f"{"Nama":<5}: ")
    while True:
        try:
            age = int(input(f"{"Umur":<5}: "))
            if age < 1:
                raise ValueError("Umur tidak boleh kurang dari 1 tahun")
            
            break
        except ValueError as e:
            if "invalid literal for int() with base 10" in str(e):
                print("Input tidak valid. Mohon masukkan angka")
            else:
                print(e)
    
    if cats_or_dogs is dogs:
        dog = Dog(name, age)
        dogs.append(dog)
        return dogs        
    else:
        cat = Cat(name, age)
        cats.append(cat)
        return cats

def delete(cats_or_dogs):
    while True:
        try:
            data_index = int(input("Masukkan nomor data yang ingin dihapus: "))
            if cats_or_dogs is cats:
                cats.pop(data_index - 1)
            else:
                dogs.pop(data_index - 1)
            break
        except ValueError as e:
            if "invalid literal for int() with base 10" in str(e):
                print("Input tidak valid. Mohon masukkan angka")
            else:
                print(e)
        except IndexError:
            print("Tidak ada data dalam index tersebut")

    if cats_or_dogs is cats:
        return cats
    else:
        return dogs   

def display(num, cats_or_dogs):
    number = 1
    if len(cats_or_dogs) == 0:
        if cats_or_dogs is cats:
            print("Tidak ada kucing di sini")
        else:
            print("Tidak ada anjing di sini")
    else:
        if cats_or_dogs is cats:
            print(f"Jumlah kucing: {num}")
        else:
            print(f"Jumlah anjing: {num}")
        for cat_or_dog in cats_or_dogs:
            print(f"{number}. {cat_or_dog.name}")
            print(f"{"Nama":<5}: {cat_or_dog.name}")
            print(f"{"Umur":<5}: {cat_or_dog.age}")
            number += 1

def display_all(num_of_dogs, num_of_cats, cats, dogs):
    if len(cats) == 0 and len(dogs) == 0:
        print("Tidak ada hewan di sini")
    else:
        display(num_of_dogs, dogs)
        print("")
        display(num_of_cats, cats)

def action(cats_or_dogs):
    sentence = ""
    if len(cats_or_dogs) == 0:
        if cats_or_dogs is cats:
            sentence += "Maaf, tidak ada kucing di sini"
        else:
            sentence += "Maaf, tidak ada anjing di sini"
    elif len(cats_or_dogs) > 1:
        for i, the_animal in enumerate(cats_or_dogs):
            if i == len(cats_or_dogs) - 1:
                sentence += "dan " + the_animal.name + " mengeluarkan suara " + the_animal.make_sound()
            else:
                sentence += the_animal.name + ', '  
    elif len(cats_or_dogs) < 2:
        for the_animal in cats_or_dogs:
            sentence += the_animal.name + " mengeluarkan suara " + the_animal.make_sound()
    print(sentence)


num_of_cats = 0
num_of_dogs = 0
cats = []
dogs = []
iteration = 0

print(f"{'=' * 5} Tempat Penangkaran Anjing dan Kucing {'=' * 5}")
while True:    
    if iteration == 0:
        print("Pilih aksi:")
    else:
        print("\nPilih aksi:")

    print("1. Tambahkan data hewan")
    print("2. Hapus data hewan")
    print("3. Tampilkan data hewan")
    print("4. Perintahkan hewan untuk bersuara")
    print("5. Keluar")

    try:
        act = int(input("Masukkan pilihan (1/2/3/4/5): "))
        if 0 < act < 6:
            if act == 1:
                print("\nData hewan yang ingin ditambahkan: ")
                print(f"1. Anjing{" " * 4}2. Kucing")                
                try:
                    species = int(input("Masukkan pilihan (1/2): "))                
                    if 0 < species < 3:
                        if species == 1:
                            num_of_dogs += 1
                            add(dogs)
                        elif species == 2:
                            num_of_cats += 1
                            add(cats)
                    else:
                        raise ValueError("Input tidak sesuai. Silahkan masukkan nomor opsi yang tersedia")
                except ValueError as e:
                    if "invalid literal for int() with base 10" in str(e):
                        print("Input tidak valid. Mohon masukkan angka")
                    else:
                        print(e)
            elif act == 2:    
                print("\nData hewan yang ingin dihapuskan: ")            
                print(f"1. Anjing{" " * 4}2. Kucing")                
                try:
                    species = int(input("Masukkan pilihan (1/2): "))                
                    if 0 < species < 3:
                        if species == 1:
                            num_of_dogs -= 1
                            delete(dogs)
                        elif species == 2:
                            num_of_cats -= 1
                            delete(cats)
                    else:
                        raise ValueError("Input tidak sesuai. Silahkan masukkan nomor opsi yang tersedia")
                except ValueError as e:
                    if "invalid literal for int() with base 10" in str(e):
                        print("Input tidak valid. Mohon masukkan angka")
                    else:
                        print(e)
            elif act == 3:
                print("\nData hewan yang ingin ditampilkan: ")
                print(f"1. Anjing{' ' * 4}2. Kucing{' ' * 4}3. Semua")
                try:
                    species = int(input("Masukkan pilihan (1/2/3): "))                
                    if 0 < species < 4:
                        if species == 1:
                            display(num_of_cats, dogs)
                        elif species == 2:
                            display(num_of_cats, cats)
                        elif species == 3:
                            display_all(num_of_dogs, num_of_cats, cats, dogs)
                    else:
                        raise ValueError("Input tidak sesuai. Silahkan masukkan nomor opsi yang tersedia")
                except ValueError as e:
                    if "invalid literal for int() with base 10" in str(e):
                        print("Input tidak valid. Mohon masukkan angka")
                    else:
                        print(e)
            elif act == 4:
                print("\nHewan yang ingin diperintahkan: ")
                print(f"1. Anjing{" " * 4}2. Kucing")                
                try:
                    species = int(input("Masukkan pilihan (1/2): "))                
                    if 0 < species < 3:
                        if species == 1:
                            action(dogs)
                        elif species == 2:                            
                            action(cats)
                    else:
                        raise ValueError("Input tidak sesuai. Silahkan masukkan nomor opsi yang tersedia")
                except ValueError as e:
                    if "invalid literal for int() with base 10" in str(e):
                        print("Input tidak valid. Mohon masukkan angka")
                    else:
                        print(e)
            elif act == 5:
                break
        else:
            raise ValueError("Invalid Input. Masukkan nomor opsi yang tersedia")
        
    except ValueError as e:
        if "invalid literal for int() with base 10" in str(e):
            print("Invalid input. Masukkan nomor opsi")
        else:
            print(e)
    
    iteration += 1