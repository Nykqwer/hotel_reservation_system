
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about_page():
    aboutPage()


class aboutPage(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
    
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 496,
            width = 1002,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1002.0,
            496.0,
            fill="#FFFFFF",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            501.0,
            237.0,
            image=self.image_image_1
        )
       
