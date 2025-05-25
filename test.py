import tkinter as tk
from clock_funcs import update_clock, close_app

root = tk.Tk()
root.title("My Clock App")

root.attributes("-fullscreen", True)
root.configure(bg="black")

time_label = tk.Label(root, font=("Helvetica", 120), fg="white", bg="black")
time_label.pack(pady=80)

date_label = tk.Label(root, font=("Helvetica", 60), fg="white", bg="black")
date_label.pack()

close_button = tk.Button(root, text="Close", command=lambda: close_app(root), font=("Helvetica", 20), bg="red", fg="white")
close_button.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

root.bind("<Escape>", lambda e: root.destroy())

update_clock(root, time_label, date_label)