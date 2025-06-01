from PIL import Image, ImageTk
import tkinter as tk

def home_button(controller, page):
    """画像のサイズを調整"""
    image = Image.open("homeicon.png").resize((50, 50))
    home_icon = ImageTk.PhotoImage(image)
    
    home_btn = tk.Button(
        page, image=home_icon,
        command=lambda: controller.show_frame("HomePage"),
        bg=page["bg"],
        activebackground=page["bg"],
        borderwidth=0,
        highlightthickness=0
    )
    home_btn.image = home_icon
    home_btn.place(relx=0.0, rely=0.0, anchor='nw', x=10, y=10)