from pathlib import Path
from tkinter import Toplevel, Canvas, Entry, Button, PhotoImage, messagebox
from db_manager.userbase import check_login
from registration import registration_window
from main_menu_work import main_window


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/login")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login_window():
    Login()


class Login(Toplevel):
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

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.login_func(entry_1, entry_2),
            relief="flat"
        )
        button_1.place(
            x=608.0,
            y=487.0,
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
            command=lambda: registration_window(),
            relief="flat"
        )
        button_2.place(
            x=515.0,
            y=486.0,
            width=77.0,
            height=35.0
        )
        
        username_image = PhotoImage(
            file=relative_to_assets("username.png"))
        img = self.canvas.create_image(
            599.0,
            355.0,
            image=username_image
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry.png"))
        entry_bg_1 = self.canvas.create_image(
            600.0,
            318.5,
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
            x=495.0,
            y=300.0,
            width=210.0,
            height=35.0
        )

        password_image = PhotoImage(
            file=relative_to_assets("password.png"))
        img = self.canvas.create_image(
            599.0,
            444.0,
            image=password_image
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry.png"))
        entry_bg_2 = self.canvas.create_image(
            600.0,
            405.5,
            image=entry_image_2
        )
    
        entry_2 = Entry(
            self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            show="*",
            highlightthickness=0
        )
        entry_2.place(
            x=495.0,
            y=387.0,
            width=210.0,
            height=35.0
        )

        PyFlora_image = PhotoImage(
            file=relative_to_assets("PyFlora.png"))
        img = self.canvas.create_image(
            600.0,
            227.0,
            image=PyFlora_image
        )

        # Essentials
        self.resizable(False, False)
        self.mainloop()

    # Login check function
    def login_func(self, entry_1, entry_2):
        entry_user = entry_1.get().lower()
        entry_pass = entry_2.get().lower()
        if check_login(entry_user, entry_pass) == True:
            #print(entry_user, entry_pass)
            self.destroy()
            main_window()
        elif (entry_user == "" or entry_pass == ""):
            messagebox.showerror(
                title="Empty field",
                message="One of the input fields is empty",
            )
        else:
            messagebox.showerror(
                title="Invalid Credentials",
                message="Invalid username or password",
            )

