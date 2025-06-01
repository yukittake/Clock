import tkinter as tk
import time
import math

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
        
        """変更"""
        controller.close_button(self, bg="black")
        #controller.home_button(self)

        self.clock_canvas = tk.Canvas(self, width=300, height=300, bg="#111111", highlightthickness=0) #add
        self.clock_canvas.pack(pady=20) #add

        self.update_clock()

    def update_clock(self):
        now = time.localtime()
        current_hour = int(time.strftime("%H", now))
        current_min = int(time.strftime("%M", now))
        current_second = int(time.strftime("%S", now))
        current_time = f"{current_hour:02d}:{current_min:02d}:{current_second:02d}"
        current_date = time.strftime("%Y-%m-%d", now)
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.draw_analog_clock(current_hour, current_min, current_second)
        self.after(1000, self.update_clock)

    def draw_analog_clock(self, hour, minute, second):
        self.clock_canvas.delete("all")
        center_x, center_y = 150, 150
        radius = 120

        # 文字盤
        self.clock_canvas.create_oval(center_x-radius, center_y-radius, center_x+radius, center_y+radius, outline="white", width=4)

        # 目盛り
        for i in range(12):
            angle = math.radians(i * 30)
            x1 = center_x + math.sin(angle) * (radius - 10)
            y1 = center_y - math.cos(angle) * (radius - 10)
            x2 = center_x + math.sin(angle) * (radius - 30)
            y2 = center_y - math.cos(angle) * (radius - 30)
            self.clock_canvas.create_line(x1, y1, x2, y2, fill="white", width=3)

        # 時針
        hour_angle = math.radians((hour % 12 + minute / 60) * 30)
        hour_x = center_x + math.sin(hour_angle) * (radius * 0.5)
        hour_y = center_y - math.cos(hour_angle) * (radius * 0.5)
        self.clock_canvas.create_line(center_x, center_y, hour_x, hour_y, fill="white", width=8)

        # 分針
        min_angle = math.radians(minute * 6)
        min_x = center_x + math.sin(min_angle) * (radius * 0.8)
        min_y = center_y - math.cos(min_angle) * (radius * 0.8)
        self.clock_canvas.create_line(center_x, center_y, min_x, min_y, fill="white", width=5)

        # 秒針
        sec_angle = math.radians(second * 6)
        sec_x = center_x + math.sin(sec_angle) * (radius * 0.9)
        sec_y = center_y - math.cos(sec_angle) * (radius * 0.9)
        self.clock_canvas.create_line(center_x, center_y, sec_x, sec_y, fill="red", width=2)

        # 中心点
        self.clock_canvas.create_oval(center_x-8, center_y-8, center_x+8, center_y+8, fill="white", outline="")