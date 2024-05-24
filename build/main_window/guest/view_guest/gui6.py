
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter.ttk import Treeview, Style
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def view_guest():
    viewGuest()


class viewGuest(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.search_query = StringVar()

        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 496,
            width = 1064,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            1064.0,
            496.0,
            fill="#FFFFFF",
            outline="")

       
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.edit_btn = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_edit,
            relief="flat"
        )
        self.edit_btn.place(
            x=574.0,
            y=419.0,
            width=190.0,
            height=48.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.delete_btn = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_delete,
            relief="flat"
        )
        self.delete_btn.place(
            x=780.0,
            y=419.0,
            width=190.0,
            height=48.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.parent.navigate("add"),
            relief="flat"
        )
        button_3.place(
            x=59.0,
            y=31.0,
            width=53.0,
            height=53.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            210.0,
            57.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            502.0,
            439.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            853.0,
            61.0,
            image=self.image_image_3
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            825.5,
            62.0,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.search_query
        )
        
        entry_1.bind(
            "<KeyRelease>",
            lambda event: self.filter_treeview_records(self.search_query.get()),
        )
        entry_1.place(
            x=782.0,
            y=50.0,
            width=87.0,
            height=22.0
        )

        canvas.create_text(
            784.0,
            52.0,
            anchor="nw",
            text="Search...",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            762.0,
            62.0,
            image=self.image_image_4
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=675.0,
            y=35.0,
            width=53.0,
            height=53.0
        )
        
        canvas.create_rectangle(
            59.0,
            97.0,
            970.0,
            398.0,
            fill="#EFEFEF",
            outline="")

        
        
        self.columns = {
            "id": ["ID", 10, ],
            "name": ["Guest Name", 50],
            "address": ["Address", 60],
            "number": ["Tel Number", 40],
            "email": ["email", 60],
        }
      
      
        # Create a style
        self.style = Style(self)
        self.style.configure("Custom.Treeview", background="#FFFFFF",justify="center")
        self.style.map("Custom.Treeview",
                       background=[("selected", "#3776F0")])
        
        self.treeview = Treeview(
            self,
            columns=list(self.columns.keys()),
            show="headings",
            height=200,
            selectmode="browse",
            style="Custom.Treeview"
            # bg="#FFFFFF",
            # fg="#5E95FF",
            # font=("Montserrat Bold", 18 * -1)
        )
        
        for idx, txt in self.columns.items():
            self.treeview.heading(idx, text=txt[0],anchor='center')
            self.treeview.column(idx, width=txt[1],anchor='center')
        
        self.treeview.place(x=59.0, y=97.0, width=911, height=301)
        #self.treeview.place(x=40.0, y=101.0, width=700.0, height=229.0)

        # Insert data
        self.handle_refresh()   

        # Add selection event
        self.treeview.bind("<<TreeviewSelect>>", self.on_treeview_select)
        
    def filter_treeview_records(self, query):
        self.treeview.delete(*self.treeview.get_children())
        # Run for loop from original data
        for row in self.guest_data:
            # Check if query exists in any value from data
            if query.lower() in str(row).lower():
                # Insert the data into the treeview
                self.treeview.insert("", "end", values=row)
        self.on_treeview_select()
    
    def on_treeview_select(self, event=None):
        try:
            self.treeview.selection()[0]
        except IndexError:
            self.parent.selected_rid = None
            return
        # Get the selected item
        item = self.treeview.selection()[0]
        # Get the room id
        self.parent.selected_rid = self.treeview.item(item, "values")[0]
        # Enable the buttons
        self.delete_btn.config(state="normal")
        self.edit_btn.config(state="normal")
        
    def handle_refresh(self):
        self.treeview.delete(*self.treeview.get_children())
        self.guest_data = db_controller.get_guest()
        for row in self.guest_data:
            self.treeview.insert("", "end", values=row)
    
    def handle_delete(self):
        if db_controller.delete_guest(self.parent.selected_rid):
            messagebox.showinfo("Success","Successfully Deleted the guest info")
        else:
            messagebox.showerror("failed","Unable to delete guest data")

        self.handle_refresh()
    
    
    def handle_edit(self):
        self.parent.navigate("edit")
        self.parent.windows["edit"].initialize()
        self.handle_refresh()
