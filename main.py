import tkinter as tk

from user_interfaces import AppInterface
from raw_attendance import RawAttendanceManager
from ui_management import UserInterfacesManagement
from visual_data_management import VisualDataManagement

if __name__ == '__main__':
    inface = AppInterface(tk.Tk())
    inface.window.title("Attandance Record")
    raw_attd = RawAttendanceManager()
    ui_management = UserInterfacesManagement(inface, raw_attd)
    vd_management = VisualDataManagement(inface, raw_attd)
    inface.window.mainloop()