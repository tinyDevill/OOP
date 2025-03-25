def add_task(tasks, new_task):
    tasks.append(new_task)
    return tasks

def delete_task(tasks, index):
    try:
        tasks.pop(index - 1)
    except IndexError:
        print(f"Tugas dengan nomor {index} tidak ditemukan")
    return tasks

def display(tasks):
    i = 1
    for task in tasks:
        print(f"{i}. {task}")
        i += 1

tasks = []

while True:
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")
    
    try:
        action = int(input("Masukkan pilihan (1/2/3/4): "))
        if 0 < action < 5:
            if action == 1:
                new_task = input("Masukkan tugas yang ingin ditambahkan: ")
                add_task(tasks, new_task)
            elif action == 2:
                task_index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                delete_task(tasks, task_index)
            elif action == 3:
                display(tasks)
            elif action == 4:
                break
        else:
            raise ValueError("Invalid Input. Masukkan nomor opsi yang tersedia")
        
    except ValueError as e:
        if "invalid literal for int() with base 10" in str(e):
            print("Invalid input. Masukkan nomor opsi")
        else:
            print(e)