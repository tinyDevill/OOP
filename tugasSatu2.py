student_num = int(input("Masukkan jumlah siswa: "))
student_marks = {}

for i in range(student_num):
    name = input(f"Masukkan nama siswa ke-{i + 1}: ")
    student_marks[name] = int(input(f"Masukkan nilai untuk {name}: "))

print(f"dictionary = {student_marks}")