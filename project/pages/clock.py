import tkinter as tk

class ClockPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, font=("Helvetica", 20), fg="white", bg="black")
        label.pack(pady=50)

        button = tk.Button(self, text="ホームに戻る", command=lambda: controller.show_frame("HomePage"))
        button.pack()
        