import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class AppInterface():
    def __init__(self, window):
        # widget
        self.window = window
        self.notebook = ttk.Notebook(self.window)
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame1a = tk.Frame(self.frame1, padx=10, pady=10)
        self.list_box = tk.Listbox(self.frame1, exportselection=False)
        self.list_box2 = tk.Listbox(self.frame1, exportselection=False)
        self.list_box3 = tk.Listbox(self.frame1, exportselection=False)
        self.fixfile_listbox = tk.Listbox(self.frame1, exportselection=False)
        self.menu_bar = tk.Menu(self.window)
        self.file_menu = tk.Menu(self.window, tearoff=0)

        self.window.geometry('800x650')
        self.window.config(menu=self.menu_bar)

        # di repair window
        self.file_title = tk.StringVar(self.window)
        self.index = tk.IntVar(self.window)
        self.index.set(0)
        self.absen_sekolah = tk.StringVar(self.window)
        self.absen_sekolah.set('empty')
        self.kecamatan = tk.StringVar(self.window)
        self.kecamatan.set('empty')
        self.kepsek = tk.StringVar(self.window)
        self.kepsek.set('empty')
        self.before = tk.StringVar(self.window)
        self.before.set('empty')
        self.sekolah = tk.StringVar(self.window)
        self.sekolah.set('empty')
        self.attd_len = tk.IntVar(self.window)
        self.attd_len.set(0)

        # frame configure
        for i in range(4):
            self.frame1.columnconfigure(index=i, weight=1, minsize=100)
        for i in range(2):
            self.frame1.rowconfigure(index=i, weight=1)

        # frame1a cell
        self.aframe1a()
        self.data_preview()

        # menu
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        # beberapa cell lain
        self.notebook.pack(fill='both', expand=True)
        self.list_box.grid(row=0, column=0, columnspan=1, sticky='wens')
        self.list_box2.grid(row=0, column=1, columnspan=2, sticky='wens')
        self.frame1a.grid(row=1, column=0, columnspan=3, sticky='wens')
        self.list_box3.grid(row=0, column=3, sticky='wens', padx=10)
        self.fixfile_listbox.grid(row=1, column=3, sticky='wens', padx=10, pady=10)

        self.notebook.add(self.frame1, text='Data Clasify')
        self.notebook.add(self.frame2, text='Data Generate')

    def data_preview(self):
        for i in range(4):
            self.frame2.columnconfigure(index=i, weight=1)
        for i in range(8):
            self.frame2.rowconfigure(index=i, weight=1)
            
    def aframe1a(self):
        for i in range(3):
            self.frame1a.grid_columnconfigure(i, weight=1)
        for i in range(8):
            self.frame1a.grid_rowconfigure(i, weight=1)
        font = tkFont.Font(size=10)
        self.title_file = tk.Label(self.frame1a, textvariable=self.file_title, font=font)
        self.title_file.grid(row=0, column=0, sticky='w')
        # panjang index
        self.label_len_attd = tk.Label(self.frame1a, text='Jumlah Attendence', font=font)
        self.label_len_attd.grid(row=1, column=0, sticky='w')
        # contain
        self.label_clen_attd = tk.Label(self.frame1a, textvariable=self.attd_len, font=font)
        self.label_clen_attd.grid(row=1, column=2, sticky='w', padx=20)
        # label index
        self.label_index = tk.Label(self.frame1a, text='Index', font=font)
        self.label_index.grid(row=2, column=0, sticky='w')
        # contain
        self.label_cindex = tk.Label(self.frame1a, textvariable=self.index, font=font)
        self.label_cindex.grid(row=2, column=2, sticky='w', padx=20)
        # label sekolah
        self.label_absensekolah = tk.Label(self.frame1a, text="Absen Sekolah", font=font, anchor='w')
        self.label_absensekolah.grid(row=3, column=0, sticky='w')
        # contain
        self.label_cabsensekolah = tk.Label(self.frame1a, textvariable=self.absen_sekolah, font=font)
        self.label_cabsensekolah.grid(row=3, column=2, sticky='w', padx=20)
        # label kecamatan
        self.label_kecamatan = tk.Label(self.frame1a, text="Kecamatan", font=font)
        self.label_kecamatan.grid(row=4, column=0, sticky='w')
        # contain
        self.label_ckecamatan = tk.Label(self.frame1a, textvariable=self.kecamatan, font=font)
        self.label_ckecamatan.grid(row=4, column=2, sticky='w', padx=20)
        # # label kepsek
        self.label_kepsek = tk.Label(self.frame1a, text="Kepsek:", font=font)
        self.label_kepsek.grid(row=5, column=0, sticky='w')
        self.label_ckepsek = tk.Label(self.frame1a, textvariable=self.kepsek, font=font)
        self.label_ckepsek.grid(row=5, column=2, sticky='w', padx=20)
        # label before
        self.label_before = tk.Label(self.frame1a, text="Before:", font=font)
        self.label_before.grid(row=6, column=0, sticky='w')
        self.label_cbefore = tk.Label(self.frame1a, textvariable=self.before, font=font)
        self.label_cbefore.grid(row=6, column=2, sticky='w', padx=20)
        # label sekolah
        self.label_sekolah = tk.Label(self.frame1a, text='Sekolah', font=font)
        self.label_sekolah.grid(row=7, column=0, sticky='w')
        self.label_csekolah = tk.Label(self.frame1a, textvariable=self.sekolah, font=font)
        self.label_csekolah.grid(row=7, column=2, sticky='w', padx=20)
        # searchbox
        self.search_box = tk.Entry(self.frame1a)
        self.search_box.grid(row=8, column=0, columnspan=3, sticky='nsew', pady=10)
        # list box
        self.list_box_a = tk.Listbox(self.frame1a)
        self.list_box_a.grid(row=9, column=0, columnspan=3, rowspan=1, sticky='nsew')
        # titik dua
        for i in range(7):        
            if i == 0:
                continue
            self.label_semikolon = tk.Label(self.frame1a, text=":", font=font).grid(row=i, column=1, sticky='w', padx=5)