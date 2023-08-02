from tkinter import *;
compiler = Tk()
compiler.title("myVSC")
menu_bar = Menu(compiler)
run_bar = Menu(menu_bar)
editor = Text()
editor.pack()
compiler.mainloop()