import tkinter as tk
from pages.home import HomePage
from pages.second import SecondPage
from pages.third import ThirdPage
from pages.clock import ClockPage

from functions.show_frame import show_frame
from functions.close_button import close_button
from functions.menu_bar import menu_bar  # ←クラスから関数に変更

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("画面切り替えデモ")
        self.attributes("-fullscreen", True)

        # 各画面（Frame）を定義
        self.frames = {}
        for F in (HomePage, SecondPage, ThirdPage, ClockPage):
            page_name = F.__name__
            frame = F(self, self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        # メニューバーを生成（関数として呼び出し）
        self.menu_bar = menu_bar(self, self)

        show_frame(self, "HomePage")
        self.menu_bar.lift_bar()
        self.bind("<Escape>", lambda e: self.destroy())

    def show_frame(self, page_name):
        show_frame(self, page_name)
        self.menu_bar.lift_bar()  # メニューバーとmenuiconを最前面に

    def close_button(self, page, **kwargs):
        close_button(self, page, **kwargs)

    def show_menu_bar(self):
        self.menu_bar.lift_bar()

if __name__ == "__main__":
    app = App()
    app.mainloop()