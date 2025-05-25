import time
import tkinter as tk

def update_clock(root, time_label, date_label):
    now = time.localtime()
    current_time = time.strftime("%H:%M:%S", now)
    current_date = time.strftime("%Y-%m-%d", now)
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, lambda: update_clock(root, time_label, date_label))

def close_app(root):
    root.destroy()