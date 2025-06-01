import tkinter as tk

class SamplePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(
            self, 
            text = "これはサンプル画面", 
            font = ("Helvetica", 20)
        )
        label.pack(pady = 50)

        button = tk.Button(
            self, 
            text = "ホーム画面へ", 
            command = lambda: controller.show_frame("HomePage")
        )
        button.pack()
        
        controller.close_button(self)