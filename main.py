from tkinter import *;
compiler = Tk()
compiler.title("myVSC")

def run():
    code = editor.get('1.0', END)
    print("code will get executed")

menu_bar = Menu(compiler)
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="RUN", command=run)
menu_bar.add_cascade(label="RUN", menu=run_bar)
compiler.config(menu=menu_bar)


editor = Text()
editor.pack()
compiler.mainloop()