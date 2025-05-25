import tkinter as tk

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="これは2つ目の画面", font=("Helvetica", 20))
        label.pack(pady=50)

        button = tk.Button(self, text="次の画面へ", command=lambda: controller.show_frame("ThirdPage"))
        button.pack()
        