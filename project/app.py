import tkinter as tk
from pages.home import HomePage
from pages.second import SecondPage
from pages.third import ThirdPage
from pages.clock import ClockPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("画面切り替えデモ")
        self.attributes("-fullscreen", True)

        # 各画面（Frame）を定義
        self.frames = {}
        for F in (HomePage, SecondPage, ThirdPage, ClockPage):
            page_name = F.__name__
            frame = F(self, self)  # 親ウィンドウとコントローラーを渡す
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("HomePage")
        self.bind("<Escape>", lambda e: self.destroy())

    def show_frame(self, page_name):
        """ 指定されたページを表示 """
        frame = self.frames[page_name]
        frame.tkraise()  # フレームを最前面に表示

if __name__ == "__main__":
    app = App()
    app.mainloop()