#大元のソースコード。これを実行すれば良い。
import tkinter as tk         #ターミナルではなく本物のアプリのように動かすための標準モジュール
                             #このソースコードと同じディレクトリに「page」というファイルを作成し、その中に以下のpythonスクリプトを入れる
from pages.home import HomePage 
from pages.second import SecondPage
from pages.third import ThirdPage
from pages.clock import ClockPage

class App(tk.Tk):            #tk.Tkクラスの継承 ex) root=tk.Tk()と定義するとメインウィンドウを表示する
    def __init__(self):      #コンストラクタ。 selfは生成されたインスタンス自身を指し、使う時には()の中になにも書く必要はないがコンストラクタ作成の際には必須
        super().__init__()   #親のコンストラクタの呼び出し。ここでtk.Tk()は行われている。
        self.title("画面切り替えデモ")            #ウィンドウの名前。tk (tkinter)のTkクラスの関数
        self.attributes("-fullscreen", True)  #ウィンドウのフルスクリーンをTrue(on)にtk (tkinter)のTkクラスの関数

        # 各画面（Frame）を定義
        self.frames = {}   #Appのインスタンス属性framesを作成し、空の辞書を代入。javaでいうインスタンス変数(フィールド)
        for F in (HomePage, SecondPage, ThirdPage, ClockPage): #importしたクラス
            page_name = F.__name__               #(クラス).__name__でクラスの名前をStringで返す。今回は"HomePage"や"SecondPage"
            frame = F(self, self)                #HomePageクラスなどのインスタンスを作成。F(self,self)→HomePage(self,self)
            self.frames[page_name] = frame       #辞書 ex) self.frames["HomePage"]→HomePage(self,self)
            frame.place(relwidth=1, relheight=1) #親ウィジェットに対しての横幅、縦幅の割合を指定して配置。つまり複数の画面が重なっている。これはtk.Frameのメソッド。

        self.show_frame("HomePage")                      #下に定義
        self.bind("<Escape>", lambda e: self.destroy())  #escapeボタンで強制終了

    def show_frame(self, page_name):
        """ 指定されたページを表示 """
        frame = self.frames[page_name]
        frame.tkraise()  # フレームを最前面に表示。tk.Frameのメソッド。

#Cでいうmain文
if __name__ == "__main__":  #このファイルが直接実行されたとき(モジュールとしてではなく)だけ、以下を実行する。__name__は特別な変数
    app = App()             #Appクラスのインスタンスを作成　ex) x= int() (intはデフォルトで0を返すのでx=0)
                            #Appのインスタンスはなにをするか見に行く
    app.mainloop()          #Tkinter では、ボタンのクリックやウィンドウの描画などのイベントを常に待ち受ける「メインループ」が必要
