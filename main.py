from tkinter import *;
compiler = Tk()
compiler.title("myVSC")

menu_bar = Menu(compiler)
run_bar = Menu(menu_bar)
run_bar.add_command(label="RUN")
menu_bar.add_cascade(label="RUN", menu=run_bar)



editor = Text()
editor.pack()
compiler.mainloop()