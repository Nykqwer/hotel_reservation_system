
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Frame, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def update_guest():
    updateGuest()


class updateGuest(Frame):
      def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_r_id = self.parent.selected_rid
        
        
        self.data = {
            "id": StringVar(),
            "name": StringVar(),
            "address": StringVar(),
            "number": StringVar(),
            "email": StringVar(),
     
        }
        
        


        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 496,
            width = 1064,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1064.0,
            496.0,
            fill="#FFFFFF",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_update,
            relief="flat"
        )
        button_1.place(
            x=762.0,
            y=238.0,
            width=190.0,
            height=48.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            136.0,
            52.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            528.0,
            249.0,
            image=self.image_image_2
        )
        
       

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            528.4999923706055,
            261.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            self,
            textvariable=self.data["email"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=401.322265625,
            y=249.0,
            width=254.35545349121094,
            height=22.0
        )

        self.canvas.create_text(
            412.20379638671875,
            251.0,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            528.0,
            147.0,
            image=self.image_image_3
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            528.4999923706055,
            159.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            self,
            textvariable=self.data["number"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=401.322265625,
            y=147.0,
            width=254.35545349121094,
            height=22.0
        )

        self.canvas.create_text(
            412.20379638671875,
            149.0,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            184.0,
            350.0,
            image=self.image_image_4
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            184.49999237060547,
            362.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            self,
            textvariable=self.data["address"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=57.322265625,
            y=350.0,
            width=254.35545349121094,
            height=22.0
        )

        self.canvas.create_text(
            68.2037353515625,
            352.0,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            184.0,
            249.0,
            image=self.image_image_5
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            184.49999237060547,
            261.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            self,
            textvariable=self.data["name"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=57.322265625,
            y=249.0,
            width=254.35545349121094,
            height=22.0
        )

        self.canvas.create_text(
            68.2037353515625,
            251.0,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.canvas.create_rectangle(
            38.0,
            68.00003051766544,
            242.0,
            70.004638671875,
            fill="#003B95",
            outline="")

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            184.0,
            147.0,
            image=self.image_image_6
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            184.49999237060547,
            159.0,
            image=entry_image_5
        )
        
    
        self.id_text = Entry(
            self,
            textvariable=self.data["id"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        self.id_text.place(
            x=57.322265625,
            y=147.0,
            width=254.35545349121094,
            height=22.0
        )

        self.canvas.create_text(
            68.2037353515625,
            149.0,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )
        
      def initialize(self):
        self.guest_data = db_controller.get_guest()
        self.selected_r_id = self.parent.selected_rid
        #self.product_data = self.parent.product_data

         # Filter out all reservations for selected id reservation
        if self.guest_data is not None:
            self.selected_guest_data = list(
                filter(lambda x: str(x[0]) == self.selected_r_id, self.guest_data)
            )

            if self.selected_guest_data:
                self.selected_guest_data = self.selected_guest_data[0]

                self.data["id"].set(self.selected_guest_data[0])
                self.data["name"].set(self.selected_guest_data[1])
                self.data["address"].set(self.selected_guest_data[2])
                self.data["number"].set(self.selected_guest_data[3])
                self.data["email"].set(self.selected_guest_data[4])
          
                
      def handle_update(self):
        result = db_controller.update_guest(
            self.selected_r_id,
            name=self.data["name"].get(),
            address=self.data["address"].get(),
            number=self.data["number"].get(),
            email=self.data["email"].get(),  
      
                  
        )

            # Check if the update was successful 
        if result:
            messagebox.showinfo("Success", "Details updated successfully")
            # Navigate back to the view window
            self.parent.navigate("view")
            # Refresh the view window to update the Treeview
            self.parent.windows.get("view").handle_refresh()
            # Clear all fields in the update frame
            for label in self.data.keys():
                self.data[label].set("")
        else:
            messagebox.showerror("Error", "Failed to update details")