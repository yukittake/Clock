def show_frame(controller, page_name):
    """ 指定されたページを表示 """
    frame = controller.frames[page_name]
    frame.tkraise()