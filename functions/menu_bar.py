import tkinter as tk
from PIL import Image, ImageTk
import os

def menu_bar(parent, controller, width=220, bg="#222", fg="#fff"):
    # 画像ディレクトリのパス
    img_dir = os.path.join(os.path.dirname(__file__), "../images")

    # メニューバー本体
    bar = tk.Frame(parent, width=width, bg=bg)
    bar.place(x=-width, y=0, relheight=1)
    bar.is_open = False

    # メニューアイテムの設定
    menu_items = [
        {
            "name": "ホーム",
            "icon": os.path.join(img_dir, "homeicon.png"),
            "page": "HomePage"
        },
        {
            "name": "時計",
            "icon": os.path.join(img_dir, "clockicon.png"),
            "page": "ClockPage"
        }
    ]

    # メニューアイテムの作成
    icons = []
    def goto_page(page_name):
        toggle_menu(close=True)
        controller.show_frame(page_name)

    base_y = 80  # メニューアイコンより下にずらす
    interval = 60
    for idx, item in enumerate(menu_items):
        icon_img = Image.open(item["icon"]).resize((32, 32))
        icon = ImageTk.PhotoImage(icon_img)
        icons.append(icon)  # 参照保持
        btn = tk.Button(
            bar,
            image=icon,
            text="  " + item["name"],
            compound="left",
            anchor="w",
            font=("Meiryo", 16),
            bg=bg,
            fg=fg,
            activebackground="#444",
            activeforeground=fg,
            bd=0,
            highlightthickness=0,
            command=lambda page=item["page"]: goto_page(page)
        )
        btn.image = icon
        btn.place(x=10, y=base_y + idx * interval, width=width - 20, height=50)

    # メニューアイコン（左上）: 色をメニューバーと同じに
    menu_icon_img = Image.open(os.path.join(img_dir, "menuicon.png")).resize((40, 40))
    menu_icon = ImageTk.PhotoImage(menu_icon_img)
    menu_btn = tk.Button(
        parent,
        image=menu_icon,
        bg=bg,
        bd=0,
        highlightthickness=0,
        activebackground="#444",
        command=lambda: toggle_menu()
    )
    menu_btn.image = menu_icon
    menu_btn.place(x=10, y=10)
    menu_btn.lift()  # 最前面に

    # クリックでメニューを閉じる処理
    def on_click_outside(event):
        # メニューが開いているときのみ
        if bar.is_open:
            # メニューバーとmenu_btnの範囲外なら閉じる
            x, y = event.x_root, event.y_root
            bar_x = bar.winfo_rootx()
            bar_y = bar.winfo_rooty()
            bar_w = bar.winfo_width()
            bar_h = bar.winfo_height()
            btn_x = menu_btn.winfo_rootx()
            btn_y = menu_btn.winfo_rooty()
            btn_w = menu_btn.winfo_width()
            btn_h = menu_btn.winfo_height()
            in_bar = (bar_x <= x <= bar_x + bar_w) and (bar_y <= y <= bar_y + bar_h)
            in_btn = (btn_x <= x <= btn_x + btn_w) and (btn_y <= y <= btn_y + btn_h)
            if not in_bar and not in_btn:
                toggle_menu(close=True)

    parent.bind_all("<Button-1>", on_click_outside, add='+')

    def toggle_menu(close=None):
        if close is not None:
            open_menu = not close
        else:
            open_menu = not bar.is_open

        if open_menu:
            animate_menu(target_x=0)
            bar.is_open = True
        else:
            animate_menu(target_x=-width)
            bar.is_open = False

    def animate_menu(target_x, step=20, delay=10):
        current_x = bar.winfo_x()
        if current_x == target_x:
            return
        direction = 1 if target_x > current_x else -1
        next_x = current_x + direction * step
        if (direction == 1 and next_x > target_x) or (direction == -1 and next_x < target_x):
            next_x = target_x
        bar.place(x=next_x, y=0)
        if next_x != target_x:
            bar.after(delay, lambda: animate_menu(target_x, step, delay))

    bar.lift_bar = lambda: (bar.lift(), menu_btn.lift())

    return bar