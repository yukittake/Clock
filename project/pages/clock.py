import tkinter as tk
import time

class ClockPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#111111")

        self.time_label = tk.Label(self, font=("Helvetica", 80), fg="white", bg="#111111")
        self.time_label.pack(pady=50)

        self.date_label = tk.Label(self, font=("Helvetica", 40), fg="white", bg="#111111")
        self.date_label.pack()

        button = tk.Button(
            self, text="ホームに戻る", 
            command=lambda: controller.show_frame("HomePage"),
            font=("Helvetica", 20), bg="blue", fg="white"
        )
        button.pack(pady=30)
        
        close_button = tk.Button(
            self, text="Close",
            command=controller.destroy,
            font=("Helvetica", 20), bg="blue", fg="white"
        )
        close_button.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

        self.update_clock()

    def update_clock(self):
        now = time.localtime()
        current_time = time.strftime("%H:%M:%S", now)
        current_date = time.strftime("%Y-%m-%d", now)
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.after(1000, self.update_clock)
