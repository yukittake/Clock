import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="これはホーム画面", font=("Helvetica", 20))
        label.pack(pady=50)

        button = tk.Button(self, text="次の画面へ", command=lambda: controller.show_frame("SecondPage"))
        button.pack()
        
        #時計のページに遷移
        button = tk.Button(self, text="時計の画面へ", command=lambda: controller.show_frame("ClockPage"))
        button.pack(pady=30)
