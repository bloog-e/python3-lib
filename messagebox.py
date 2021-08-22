from tkinter import *
def askokcancel(title='',prompt='',btn=None,btn_info='',timeout=None):
    """ option : title ,prompt are a string, btn is the sowed text of the info button,
btn_info is the info and timeout is the timeout
this fonction is usefull to ask ok or cancel with more info"""
    root=Tk()
    root.title(title)
    root.result=False
    def aff_info():
        fen=Tk()
        fen.title(btn)
        label_info = Label(fen,text=btn_info)
        button_ok = Button(fen,text='OK',command=fen.destroy)
        label_info.pack()
        button_ok.pack()
        fen.mainloop()
    def ok():
        root.destroy()
        root.result = True
    def cancel():
        root.destroy()
    label_prompt = Label(root,text=prompt)
    if btn is not None:button_aff_info = Button(root,text=btn,command=aff_info)
    button_ok = Button(root,text='Ok',command=ok)
    button_cancel = Button(root,text="cancel",command=cancel)
    label_prompt.pack()
    if btn is not None:button_aff_info.pack()
    button_ok.pack(side=RIGHT)
    button_cancel.pack(side=LEFT)
    if timeout!=None:root.after(timeout,cancel)
    root.mainloop()
    return root.result