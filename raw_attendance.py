import openpyxl as xl
import datetime as dt
import calendar

import csv
from tkinter import filedialog
from tkinter import messagebox
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class RawAttendanceManager():
    def __init__(self):
        self.month = {month: [] for month in calendar.month_name[1:]}
        self.item_selected = [0, 0, 0]
        self.primary_data = []
        self.worksheet = xl.Workbook.active
        
    def manage_worksheet(self):
        # mengambil semua nama bulan yang ada di dalam data
        for i, row in enumerate(self.worksheet.iter_rows()):
            if isinstance(row[0].value, dt.datetime): # lihat apakah item ini adalah datetime
                month = row[0].value.strftime('%B') # ambil nama bulan di time datetime
                for key, value in self.month.items():
                    if key == month: # jika key dict sama dengan month maka masukan data tersebut di array dict
                        value.append([row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value])

    def get_absent_dates(self, date, month):
        dates = []
        for row in self.month[month]:
            if date == row[0].strftime('%d'):
                dates.append(row)
        return dates
    
    def get_date_in_month(self, month):
        date = []
        for row in self.month[month]:
            row_date = row[0].strftime('%d')+" "+row[0].strftime('%A')
            if not self.find_value(date, row_date):
                date.append(row_date)
        return date

    def write_identify_not_identify(self, month, date):
        if len(self.primary_data) > 0:
            classify = self.classify_data(self.get_absent_dates(date, month))
            messagebox.showinfo('Saving Data', 'identify and not identify data are successfull!!!')
            with open('Result/Data/'+month+'_'+date+'_identify'+'.csv', 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                for row in classify[0]:
                    writer.writerow(row)
            with open('Result/Data/'+month+'_'+date+'_notIdentify'+'.csv', 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                for row in classify[1]:
                    writer.writerow(row)
        else:
            self.open_file_sekolah()
                
    def open_file(self, file_type):
        if file_type == "excel":
            file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")])
            if file_path:
                self.workbook = xl.load_workbook(file_path, read_only=True)
                self.worksheet = self.workbook.active
                self.manage_worksheet()
            else:
                print("No file selected")
        elif file_type == "text":
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.primary_data = f.read().splitlines()
            else:
                print("No file selected")
        else:
            print("Invalid file type")

    def normalize_school_name(self, school_name):
        if school_name:
            school_name = school_name.replace('.', '').replace('/', '').lower().replace('sdn ', 'sdnegeri').replace('sdn1', 'sdnegeri1')
            school_name = school_name.replace('smpn', 'smpnegeri').replace(' ', '').replace('\n', '')
            return school_name
        else:
            return ""
    
    def shool_name_score(self, school_name):
        matches = process.extractOne(school_name, self.primary_data, scorer=fuzz.token_sort_ratio)
        if matches[1] >= 80:
            return matches[0]
        else:
            return school_name
        
    # fungsi untuk memfilter data yang dapat diidentifikasi dan tidak dapat diidentifikasi
    def classify_data(self, absen_sekolah):
        identify_data = []
        not_identify_data = []

        for absen in absen_sekolah:
            identified = False
            absen[2] = self.shool_name_score(absen[2])
            for sekolah in self.primary_data:
                if self.normalize_school_name(absen[2]) == self.normalize_school_name(sekolah):
                    absen[4] = self.convert_time(absen[0])
                    identify_data.append(absen)
                    identified = True
                    break

            if not identified:
                absen[4] = self.convert_time(absen[0])
                not_identify_data.append(absen)

        return (identify_data, not_identify_data)

    # fungsi untuk mengidentifikasi setiap data apakah pagi atau sore
    def convert_time(self, date):
        if isinstance(date, dt.datetime) and date.hour >= 0 and date.hour < 12:
            return 'pagi'
        else:
            return 'sore'
        
    def find_value(self, arr, nilai):
        for i in range(len(arr)):
            if arr[i] == nilai:
                return True
        return False
    