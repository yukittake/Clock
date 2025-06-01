import tkinter as tk

def close_button(controller, page, text="Close", font=("Helvetica", 20), bg="blue", fg="white", relx=1.0, rely=1.0, anchor='se', x=-20, y=-20):
    close_btn = tk.Button(
        page, text=text,
        command=controller.destroy,
        font=font, bg=bg, fg=fg,
    )
    close_btn.place(relx=relx, rely=rely, anchor=anchor, x=x, y=y)