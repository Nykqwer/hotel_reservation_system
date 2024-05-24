
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8

from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage
from build.main_window.reservation.add_reservation.gui8 import addRes
from build.main_window.reservation.view_reservation.gui9 import viewRes
from build.main_window.reservation.update_reservation.gui10 import updateRes
#mport controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def reservation():
    Reservation()
    

class Reservation(Frame):
     def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.configure(bg="#FFFFFF")
        #self.product_data = db_controller.get_product()
          # Insert data
        
        self.windows = {
          "add": addRes(self),
          "view": viewRes(self),
          "edit": updateRes(self)

        }
        
        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=1064, height=496)
    
        self.current_window.tkraise()

     def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1064, height=496)