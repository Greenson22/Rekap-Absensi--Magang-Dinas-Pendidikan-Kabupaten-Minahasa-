import tkinter as tk
import os
import csv

from tkinter import messagebox
from mother import path

class UserInterfacesManagement():
    def __init__(self, user_interfaces, raw_attd) -> None:
        self.inface = user_interfaces
        self.raw_attd = raw_attd

        self.absen_sekolah = []
        self.before_absen_sekolah = []

        self.inface.list_box.bind("<<ListboxSelect>>", self.on_item_selected)
        self.inface.list_box2.bind("<Return>", self.on_return_key_pressed)
        self.inface.list_box3.bind('<Button-3>', self.show_list_file_menu)
        self.inface.fixfile_listbox.bind('<Button-3>', self.show_list_fixfile_menu)
        self.inface.list_box_a.bind('<<ListboxSelect>>', self.listbox_a_selected)
        self.inface.frame1a.bind('<Button-3>', self.show_repair_menu)
        self.inface.window.bind('<Key>', self.key_click)
        self.inface.search_box.bind('<Key>', self.recommended)

        self.inface.file_menu.insert_command(0, label='Open Attendance', command=self.open_absens)
        self.inface.file_menu.insert_command(1, label='Open Sekolah', command=lambda: self.raw_attd.open_file('text'))
        
        self.list_box_refresh()
    
    def open_absens(self):
        if len(self.raw_attd.primary_data) == 0:
            messagebox.showwarning("Data Sekolah", "Data Sekolah Kosong, harap diisi terlebih dahulu")
            self.raw_attd.open_file('text')
        else:
            self.raw_attd.open_file('excel')
        self.generate_listbox()

    def on_return_key_pressed(self, event):
        date = self.inface.list_box2.get(self.inface.list_box2.curselection()).split(" ")[0]
        month = self.inface.list_box.get(self.inface.list_box.curselection())
        self.raw_attd.write_identify_not_identify(month, date)
        self.list_box_refresh()
    
    def list_box_refresh(self):
        self.inface.list_box3.delete(0, tk.END)
        self.inface.fixfile_listbox.delete(0, tk.END)

        for i, file in enumerate(os.listdir(path['data'])):
            self.inface.list_box3.insert(i, str(file))
        for i, file in enumerate(os.listdir(path['fix'])):
            self.inface.fixfile_listbox.insert(i, str(file))

    def generate_listbox(self):
        print("listbox di generate")
        index = 0
        for key, value in self.raw_attd.month.items():
            if len(value) > 0:
                self.inface.list_box.insert(index, str(key))
                index += 1

    def on_item_selected(self, event):
        selected_item = self.inface.list_box.curselection()
        if selected_item:
            # month = self.inface.list_box.get(self.inface.list_box.curselection())
            self.inface.list_box2.delete(0, tk.END)
            month_data = self.raw_attd.get_date_in_month(event.widget.get(event.widget.curselection()))
            for i, row in enumerate(month_data):
                self.inface.list_box2.insert(i, str(row))

    def listbox_a_selected(self, event):
        if self.inface.list_box_a.curselection():
            index = self.inface.list_box_a.curselection()[0]
            value = self.inface.list_box_a.get(index)
            self.inface.sekolah.set(value)

    # fungsi untuk rekomendasi nama sekolah
    def recommended(self, event):
        if len(self.raw_attd.primary_data) == 0:
            messagebox.showerror("Daftar Nama Sekolah Kosong", "Tolong Diisi terlebih dahulu!!")
            self.raw_attd.open_file('text')
            return 
        self.inface.list_box_a.delete(0, tk.END)
        query = self.inface.search_box.get()
        matches = [word for word in self.raw_attd.primary_data if query.lower() in word.lower()]
        # memasukan nilai di listbox
        for i in matches:
            self.inface.list_box_a.insert(tk.END, i)

    def merge_name(self):
        if len(self.absen_sekolah) > 0:
            self.absen_sekolah[self.inface.index.get()][2] = self.inface.sekolah.get()

    def open_absen(self, file_name):
        self.absen_sekolah.clear()
        self.before_absen_sekolah.clear()
        self.inface.index.set(0)
        self.inface.file_title.set(file_name)
        with open(path['data']+file_name, 'r') as csvreader:
            csvreader = csv.reader(csvreader, delimiter=',', quotechar='"')
            for row in csvreader:
                self.absen_sekolah.append(row)
                self.before_absen_sekolah.append(row.copy())
        self.refresh()
    
    def lr_btn_click(self, right=True):
        if right:
            if self.inface.index.get() + 1 <= len(self.absen_sekolah)-1:
                self.inface.index.set(self.inface.index.get() + 1)
            else:
                self.inface.index.set(len(self.absen_sekolah)-1)
        else:
            if self.inface.index.get() - 1 >= 0:
                self.inface.index.set(self.inface.index.get()-1)
            else:
                self.inface.index.set(0)
        self.refresh()
    
    def key_click(self, event):
        if event.keysym == 'Left':
            self.lr_btn_click(False)
        elif event.keysym == 'Right':
            self.lr_btn_click(True)
        elif event.keysym == 'Return':
            self.merge_name()
            self.refresh()
    
    def refresh(self):
        if len(self.absen_sekolah) > 0:
            self.inface.absen_sekolah.set(self.absen_sekolah[self.inface.index.get()][2])
            self.inface.kecamatan.set(self.absen_sekolah[self.inface.index.get()][1])
            self.inface.kepsek.set(self.absen_sekolah[self.inface.index.get()][3])
            self.inface.before.set(self.before_absen_sekolah[self.inface.index.get()][2])
            self.inface.attd_len.set(len(self.absen_sekolah))
        
    def show_list_file_menu(self, event):
        menu = tk.Menu(self.inface.window, tearoff=0)
        menu.add_command(label="Repair", command=lambda:self.open_absen(self.inface.list_box3.get(self.inface.list_box3.curselection())))
        menu.add_command(label="Delete", command=lambda:self.delete_item_on_list_box(event, path['data']))
        menu.add_command(label="Delete All", command=lambda:self.delete_item_on_list_box(event, path['data'], delete_all=True))
        menu.post(event.x_root, event.y_root)
    
    def show_list_fixfile_menu(self, event):
        menu = tk.Menu(self.inface.window, tearoff=0)
        menu.add_command(label="Delete", command=lambda:self.delete_item_on_list_box(event, path['fix']))
        menu.add_command(label="Delete All", command=lambda:self.delete_item_on_list_box(event, path['fix'], delete_all=True))
        menu.post(event.x_root, event.y_root)
    
    def show_repair_menu(self, event):
        menu = tk.Menu(self.inface.window, tearoff=0)
        menu.add_command(label="Save", command=self.save_repair_not_identify_data)
        menu.add_command(label="Merge", command=self.merge_identify_and_not_identify_data)
        menu.post(event.x_root, event.y_root)
    
    def delete_item_on_list_box(self, event, path, delete_all=False):
        selected = event.widget.curselection()
        if selected:
            if delete_all:
                confirm = messagebox.askyesno('Konfirmasi', " Menghapus semua file yang ada di "+path)
                if confirm:
                    for file in os.listdir(path):
                        os.remove(path+file)
            else:
                item = event.widget.get(selected)
                if os.path.exists(path+item):
                    os.remove(path+item)
                else:
                    messagebox.showwarning("File tidak ada", "File yang ingin dihapus "+item+", tidak ditemukan")
        self.list_box_refresh()
                

    def save_repair_not_identify_data(self):
        with open(path['data']+self.inface.file_title.get(), mode='w', newline='') as output_file:
            writer = csv.writer(output_file)
            for row in self.absen_sekolah:
                writer.writerow(row)
    
    def merge_identify_and_not_identify_data(self):
        self.save_repair_not_identify_data()
        # mengambil file
        target_file = self.inface.file_title.get()
        target_file_piece = target_file.split('_')
        result_file = []
        for file_name in os.listdir(path=path['data']):
            piece = file_name.split('_')
            if target_file_piece[0] == piece[0] and target_file_piece[1] == piece[1]:
                result_file.append(file_name)
        
        # membaca file
        merge_data = []
        for file_name in result_file:
            with open(path['data']+file_name, mode='r') as csvreader:
                csvreader = csv.reader(csvreader, delimiter=',', quotechar='"')
                for row in csvreader:
                    merge_data.append(row)

        # menggabung kedua file
        with open(path['fix']+target_file_piece[0]+' '+target_file_piece[1]+'.csv', mode='w', newline='') as output_file:
            writer = csv.writer(output_file)
            for row in merge_data:
                writer.writerow(row)
        
        self.list_box_refresh()
    
