import tkinter as tk
from tkinter import messagebox, Menu
import datetime
import json
import os

def showabout():
    messagebox.showinfo("Tentang", "Program ini dibuat oleh Abi Sholihan")

def handle_click(tombol_diklik):
    global tombol_terpilih

    if tombol_terpilih and tombol_terpilih != tombol_diklik:
        tombol_terpilih.config(bg = '#547792', foreground = '#94B4C1')

    tombol_diklik.config(bg = '#94B4C1', foreground = '#213448')
    tombol_terpilih = tombol_diklik

def show_buttons_at_start():
    if os.path.exists("savenote.json") and os.path.getsize("savenote.json") > 0:
        with open("savenote.json", "r") as file:
            data = json.load(file)
            for entry in data:
                button = tk.Button(bleft_frame, text = entry["title"], font = ("Cascadia Code", 9), bg = '#547792', foreground = '#94B4C1', relief = "flat", command = lambda desc = entry["description"], date = entry["date"], the_title = entry["title"]: show_description("Dibuat pada " + date + "\n\n" + desc, desc_box, the_title))
                button.pack(side = "top", fill = "x", pady = (5, 0), padx = (5, 0), anchor = "w")
                button.bind("<Button-1>", lambda event, btn = button: handle_click(btn))
                button.config(width = 25, height = 2)

def make_button(title, description, date):
    button = tk.Button(bleft_frame, text = title, font = ("Cascadia Code", 9), bg = '#547792', foreground = '#94B4C1', relief = "flat", command = lambda desc = description: show_description("Dibuat pada " + date + "\n\n" + desc, desc_box, title))
    button.pack(side = "top", fill = "x", pady = (5, 0), padx = (5, 0), anchor = "w")
    button.bind("<Button-1>", lambda event, btn = button: handle_click(btn))
    button.config(width = 25, height = 2)

def show_description(description, desc_box, title):
    global choosen_button
    choosen_button = title

    desc_box.delete("1.0", tk.END)
    desc_box.insert(tk.END, description)

def save_data(the_window, content):
    title = input_title.get().upper()
    description = content.get("1.0", tk.END).strip()
    
    if title and description:
        new_entry = {
            "title": title,
            "description": description,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        existing_data = []
        if os.path.exists("savenote.json") and os.path.getsize("savenote.json") > 0:
            with open("savenote.json", "r") as file:
                existing_data = json.load(file)
        
        existing_data.append(new_entry)
        
        try:
            with open("savenote.json", "w") as file:
                json.dump(existing_data, file, indent = 4)

                success_message = tk.Toplevel(window, bg = '#213448')
                success_text = tk.Label(success_message, text = "Data berhasil disimpan!", font = ("Cascadia Code", 9), bg = '#213448', foreground = '#ECEFCA')
                success_text.pack(side = "top", pady = 10, padx = 10)
        except Exception as e:
            error_message = tk.Toplevel(window, bg = '#213448')
            error_text = tk.Label(error_message, text = f"Error: {str(e)}", font = ("Cascadia Code", 9), bg = '#213448', foreground = '#ECEFCA')
            error_text.pack(side = "top", pady = 10, padx = 10)

    make_button(title, description, new_entry["date"])
    input_title.delete(0, tk.END)
    content.delete("1.0", tk.END)
    the_window.after(0, the_window.destroy())

def input_description():
    desc_window = tk.Toplevel(window, bg = '#213448')
    desc_window.title("Deskripsi Catatan")
    desc_window.geometry("300x200")
    
    the_title = '"' + input_title.get().upper() + '"'
    label_title = tk.Label(desc_window, text = (the_title), font = ("Cascadia Code", 9), bg = '#213448', foreground = '#94B4C1', bd = 0)
    label_title.pack(side = "top", pady = (10, 0), padx = 10)

    desc_frame = tk.Frame(desc_window, bg = '#213448')
    desc_frame.pack(side = "top", fill = "both")

    label_text = tk.Label(desc_frame, text = "Masukkan Deskripsi Catatan :", font = ("Cascadia Code", 9), bg = '#213448', foreground = '#94B4C1')
    label_text.pack(side = "top", pady = (0, 5), padx = 10, anchor = "w")

    text_area = tk.Text(desc_frame, font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat")
    text_area.pack(side = "top", fill = "x", padx = 10, pady = (0, 10))
    text_area.config(height = 6, width = 30)

    save_button = tk.Button(desc_frame, text = "Simpan Catatan", font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat", command = lambda: save_data(desc_window, text_area))
    save_button.pack(side = "top", pady = (0, 10), padx = 10, anchor = "e")

def delete_dict():
    global choosen_button
    if choosen_button:
        global tombol_terpilih
        tombol_terpilih = None
        with open("savenote.json", "r") as file:
            data = json.load(file)
        
        data = [entry for entry in data if entry["title"] != choosen_button]

        with open("savenote.json", "w") as file:
            json.dump(data, file, indent = 4)

        for widget in bleft_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        show_buttons_at_start()
        desc_box.delete("1.0", tk.END)
        choosen_button = None
    else:
        None

def save_edit(data, index, edit_window, edit_box, edit_desc_box):
    edited_title = edit_box.get("1.0", tk.END).strip()
    edited_desc = edit_desc_box.get("1.0", tk.END).strip()
    if edited_title and edited_desc:
        data[index]["title"] = edited_title.upper()
        data[index]["description"] = edited_desc
        data[index]["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("savenote.json", "w") as file:
            json.dump(data, file, indent = 4)

        edit_window.destroy()
        global tombol_terpilih
        tombol_terpilih = None

        for widget in bleft_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        show_buttons_at_start()
        desc_box.delete("1.0", tk.END)

def edit_dict():
    global choosen_button
    if choosen_button:
        with open("savenote.json", "r") as file:
            data = json.load(file)

        for i, entry in enumerate(data):
            if entry["title"] == choosen_button:
                index = i
                break
        
        edit_window = tk.Toplevel(window, bg = '#213448')
        edit_window.title("Edit Catatan")

        label_title = tk.Label(edit_window, text = "Judul Catatan :", font = ("Cascadia Code", 9), bg = '#213448', foreground = '#94B4C1')
        label_title.grid(row = 0, column = 0, padx = (10, 5), pady = (10, 5))
        label_title.config(width = 15)

        title_before_edit = data[index]["title"]
        edit_box = tk.Text(edit_window, font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat")
        edit_box.insert(tk.END, title_before_edit)
        edit_box.grid(row = 0, column = 1, padx = (5, 10), pady = (10, 5))
        edit_box.config(height = 1, width = 30)

        label_desc = tk.Label(edit_window, text = "Deskripsi Catatan :", font = ("Cascadia Code", 9), bg = '#213448', foreground = '#94B4C1')
        label_desc.grid(row = 1, column = 0, padx = (10, 5), pady = (10, 5))
        label_desc.config(width = 15)

        desc_before_edit = data[index]["description"]
        edit_desc_box = tk.Text(edit_window, font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat")
        edit_desc_box.insert(tk.END, desc_before_edit)
        edit_desc_box.grid(row = 1, column = 1, padx = (5, 10), pady = (10, 5))
        edit_desc_box.config(height = 6, width = 30)

        save_button = tk.Button(edit_window, text = "Simpan Perubahan", font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat", command = lambda: save_edit(data, index, edit_window, edit_box, edit_desc_box))
        save_button.grid(row = 2, column = 1, padx = (5, 10), pady = (10, 5), sticky = "e")
        save_button.config(width = 15)


window = tk.Tk()
window.title("Catatan Harian")

menubar = tk.Menu(window)
window.config(menu = menubar)

file_menu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Keluar", command = window.quit)

about_menu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Bantuan", menu = about_menu)
about_menu.add_command(label = "Tentang", command = lambda: showabout())

top_frame = tk.Frame(window, bg = '#213448')
top_frame.pack(side = "top", fill = "x")

label1 = tk.Label(top_frame, text = "Judul Catataan :", font = ("Cascadia Code", 9), bg = '#213448', foreground = '#94B4C1')
label1.grid(row = 0, column = 0, padx = (10, 5), pady = (10, 5))

input_title = tk.Entry(top_frame, font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat", width = 45)
input_title.grid(row = 0, column = 1, padx = (5, 10), pady = (10, 5))

add_button = tk.Button(top_frame, text = "Tambah Catatan", font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat", command = input_description)
add_button.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "e")

bleft_frame = tk.Frame(window, bg = '#547792')
bleft_frame.pack(side = "left", expand = True, padx = 0, pady = 0, fill = "both")

list_label = tk.Label(bleft_frame, text = "DAFTAR CATATAN :", font = ("Cascadia Code", 9), bg = '#547792', foreground = '#ECEFCA')
list_label.pack(side = "top", pady = (10, 0), padx = 10)
list_label.config(width = 25)

tombol_terpilih = None
show_buttons_at_start()

bright_frame = tk.Frame(window, bg = '#94B4C1')
bright_frame.pack(side = "right", expand = True, padx = 0, pady = 0, fill = "both")

desc_box = tk.Text(bright_frame, font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat")
desc_box.grid(row = 0, column = 0, padx = 15, pady = 10, sticky = "nsew")

frame_to_rbutton = tk.Frame(bright_frame, bg = '#94B4C1')
frame_to_rbutton.grid(row = 1, column = 0, padx = 15, pady = (0, 10), sticky = "ne")

remove_button = tk.Button(frame_to_rbutton, text = "Hapus Catatan", font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat", command = lambda: delete_dict())
remove_button.pack(side = "top", pady = (0, 10), padx = 10, anchor = "e")

edit_button = tk.Button(frame_to_rbutton, text = "Edit Catatan", font = ("Cascadia Code", 9), bg = '#94B4C1', foreground = '#213448', relief = "flat", command = lambda: edit_dict())
edit_button.pack(side = "top", pady = (0, 10), padx = 10, anchor = "e")

window.mainloop()