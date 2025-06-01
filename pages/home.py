import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="これはホーム画面", font=("Helvetica", 20))
        label.pack(pady=50)

        button = tk.Button(self, text="次の画面へ", command=lambda: controller.show_frame("SecondPage"))
        button.pack()
        
        button = tk.Button(self, text="時計の画面へ", command=lambda: controller.show_frame("ClockPage"))
        button.pack(pady=30)
        
        controller.close_button(self, text="閉じる", anchor="ne", relx=1.0, rely=0.0, x=-20, y=20)
