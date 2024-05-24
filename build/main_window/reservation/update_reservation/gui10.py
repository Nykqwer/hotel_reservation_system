
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



def update_res():
    updateRes()


class updateRes(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_r_id = self.parent.selected_rid
        
        
        self.data = {
            "id": StringVar(),
            "guestId": StringVar(),
            "roomNo": StringVar(),
            "typeRoom": StringVar(),
            "checkIn": StringVar(),
            "checkOut": StringVar(),
     
        }
        


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
            471.7079162597656,
            fill="#FFFFFF",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            553.0,
            308.89501953125,
            image=self.image_image_1
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            553.4999923706055,
            320.495174407959,
            image=entry_image_1
        )
        entry_1 = Entry(
            self,
            textvariable=self.data["checkOut"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=426.322265625,
            y=309.0828857421875,
            width=254.35545349121094,
            height=20.82457733154297
        )

        canvas.create_text(
            437.203857421875,
            310.98486328125,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            190.0,
            46.432861328125,
            image=self.image_image_2
        )

        canvas.create_rectangle(
            55.0,
            60.76616104176901,
            330.50000012101054,
            62.77713946951553,
            fill="#003B95",
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
            x=788.0,
            y=201.0,
            width=238.0,
            height=45.64915466308594
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            553.0,
            211.890625,
            image=self.image_image_3
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            553.4999923706055,
            223.49065780639648,
            image=entry_image_2
        )
        entry_2 = Entry(
            self,
            textvariable=self.data["checkIn"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=426.322265625,
            y=212.078369140625,
            width=254.35545349121094,
            height=20.82457733154297
        )

        canvas.create_text(
            437.203857421875,
            213.98046875,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            553.0,
            114.8861083984375,
            image=self.image_image_4
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            553.4999923706055,
            126.48626327514648,
            image=entry_image_3
        )
        entry_3 = Entry(
            self,
            textvariable=self.data["roomNo"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=426.322265625,
            y=115.073974609375,
            width=254.35545349121094,
            height=20.82457733154297
        )

        canvas.create_text(
            437.203857421875,
            116.97607421875,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(
            202.0,
            310.0,
            image=self.image_image_5
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            193.49999237060547,
            321.6002769470215,
            image=entry_image_4
        )
        entry_4 = Entry(
            self,
            textvariable=self.data["typeRoom"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=66.322265625,
            y=310.18798828125,
            width=254.35545349121094,
            height=20.82457733154297
        )

        canvas.create_text(
            77.20361328125,
            312.0899658203125,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(
            202.0,
            212.0,
            image=self.image_image_6
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            202.49999237060547,
            223.60027694702148,
            image=entry_image_5
        )
        entry_5 = Entry(
            self,
            textvariable=self.data["guestId"],
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry_5.place(
            x=75.322265625,
            y=212.18798828125,
            width=254.35545349121094,
            height=20.82457733154297
        )

        canvas.create_text(
            86.20361328125,
            214.090087890625,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            202.0,
            126.0,
            image=self.image_image_7
        )

        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(
            202.49999237060547,
            137.60027694702148,
            image=entry_image_6
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
            x=75.322265625,
            y=126.18798828125,
            width=254.35545349121094,
            height=20.82457733154297
        )

        canvas.create_text(
            86.20361328125,
            128.090087890625,
            anchor="nw",
            text="Jane Doe",
            fill="#000000",
            font=("Montserrat SemiBold", 17 * -1)
        )
        
    def initialize(self):
        self.reservation_data = db_controller.get_reservation()
        self.selected_r_id = self.parent.selected_rid
        #self.product_data = self.parent.product_data

         # Filter out all reservations for selected id reservation
        if self.reservation_data is not None:
            self.selected_reservation_data = list(
                filter(lambda x: str(x[0]) == self.selected_r_id, self.reservation_data)
            )

            if self.selected_reservation_data :
                self.selected_reservation_data = self.selected_reservation_data [0]

                self.data["id"].set(self.selected_reservation_data[0])
                self.data["guestId"].set(self.selected_reservation_data[1])
                self.data["roomNo"].set(self.selected_reservation_data[2])
                self.data["typeRoom"].set(self.selected_reservation_data[3])
                self.data["checkIn"].set(self.selected_reservation_data[4])
                self.data["checkOut"].set(self.selected_reservation_data[5])
                
    def handle_update(self):
        result = db_controller.update_reservation(
            self.selected_r_id,
            guestId=self.data["guestId"].get(),
            roomNo=self.data["roomNo"].get(),
            typeRoom=self.data["typeRoom"].get(),
            checkIn=self.data["checkIn"].get(),
            checkOut=self.data["checkOut"].get(),  
      
                  
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