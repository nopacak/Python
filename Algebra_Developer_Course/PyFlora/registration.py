
from pathlib import Path
from tkinter import Toplevel, Canvas, Entry, Button, PhotoImage, messagebox
from db_manager.userbase import add_user



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/registration")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def registration_window():
    Registration()


class Registration(Toplevel):

    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)
        logo = PhotoImage(file=ASSETS_PATH / "peony_logo.png")
        self.iconphoto(True, logo)
        self.title("PyFlora App")
        self.geometry("1199x641")
        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 641,
            width = 1199,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            469.0, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        background_image = PhotoImage(
            file=relative_to_assets("background.png"))
        img = self.canvas.create_image(
            599.0,
            320.0,
            image=background_image
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry.png"))
        img = self.canvas.create_image(
            376.5,
            184.0,
            image=entry_image_1
        )
        entry_1 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=271.0,
            y=166.0,
            width=211.0,
            height=30.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry.png"))
        img = self.canvas.create_image(
            376.5,
            184.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=271.0,
            y=236.0,
            width=211.0,
            height=30.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry.png"))
        img = self.canvas.create_image(
            376.5,
            184.0,
            image=entry_image_3
        )
        entry_3 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=271.0,
            y=306.0,
            width=211.0,
            height=30.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry.png"))
        img = self.canvas.create_image(
            376.5,
            184.0,
            image=entry_image_4
        )
        entry_4 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            show="*",
            highlightthickness=0
        )
        entry_4.place(
            x=271.0,
            y=376.0,
            width=211.0,
            height=30.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry.png"))
        img = self.canvas.create_image(
            376.5,
            184.0,
            image=entry_image_5
        )
        entry_5 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            show="*",
            highlightthickness=0
        )
        entry_5.place(
            x=271.0,
            y=446.0,
            width=211.0,
            height=30.0
        )

        entry_fields = [entry_1, entry_2, entry_3, entry_4, entry_5]

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.check_form(entry_fields),
            relief="flat"
        )
        button_1.place(
            x=923.0,
            y=478.0,
            width=77.0,
            height=34.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.clear_entry_fields(entry_fields),
            relief="flat"
        )
        button_2.place(
            x=797.0,
            y=478.0,
            width=77.0,
            height=35.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(),
            relief="flat"
        )
        button_3.place(
            x=967.0,
            y=37.0,
            width=165.0,
            height=34.0
        )        

        first_name_image = PhotoImage(
            file=relative_to_assets("first_name.png"))
        img = self.canvas.create_image(
            577.0,
            185.0,
            image=first_name_image
        )

        last_name_image = PhotoImage(
            file=relative_to_assets("last_name.png"))
        img = self.canvas.create_image(
            577.0,
            255.0,
            image=last_name_image
        )

        username_image = PhotoImage(
            file=relative_to_assets("username.png"))
        img = self.canvas.create_image(
            577.0,
            325.0,
            image=username_image
        )

        password_image = PhotoImage(
            file=relative_to_assets("password.png"))
        img = self.canvas.create_image(
            577.0,
            395.0,
            image=password_image
        )

        repeat_password_image = PhotoImage(
            file=relative_to_assets("repeat_password.png"))
        img = self.canvas.create_image(
            577.0,
            465.0,
            image=repeat_password_image
        )

        PyFlora_image = PhotoImage(
            file=relative_to_assets("PyFlora.png"))
        img = self.canvas.create_image(
            126.0,
            54.0,
            image=PyFlora_image
        )

        # Essentials
        self.resizable(False, False)
        self.mainloop()


    def clear_entry_fields(self, entry_fields: list) -> None:
        for entry in entry_fields:
            entry.delete(0, "end")

    
    def check_form(self, entry_fields: list) -> None:
        data = []
        if entry_fields[3].get() == entry_fields[4].get():
            for entry in entry_fields:
                data.append(entry.get())
            #print(len(data))
            if data.count("") != 0:
                messagebox.showerror("Empty field", "At least one of the input fields is empty",
                )
                data.clear()
            else:
                if add_user(data[0], data[1], data[2], data[3]) == True:
                    messagebox.showinfo("Success!","User details successfully saved")
                else:
                    messagebox.showerror("Username unavailable","Username unavailable, choose another one")
                data.clear()
        else:
            messagebox.showerror("Password mismatch","Entered passwords do not match")