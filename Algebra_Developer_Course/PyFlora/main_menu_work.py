from pathlib import Path
from tkinter import Toplevel, Canvas, Entry, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/main_menu")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def main_window():
    Main()

class Main(Toplevel):

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

#main_window()