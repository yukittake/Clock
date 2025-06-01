import tkinter as tk

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="これは3つ目の画面", font=("Helvetica", 20))
        label.pack(pady=50)

        button = tk.Button(self, text="ホームに戻る", command=lambda: controller.show_frame("HomePage"))
        button.pack()
        
        """以下追加"""
        controller.close_button(self)
        #controller.home_button(self)