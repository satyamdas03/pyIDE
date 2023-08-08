from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

BACKGROUND_COLOR = "#1E1E1E"
TEXT_COLOR = "#FFFFFF"
HIGHLIGHT_COLOR = "#404040"

compiler = Tk()
compiler.title("myVSC")
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='code save bhi karna hota hai')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

# Configure dark mode color scheme
compiler.configure(bg=BACKGROUND_COLOR)
editor = Text(compiler, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)  # Set cursor color to white
code_output = Text(compiler, height=10, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)  # Set cursor color to white
menu_bar = Menu(compiler, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
file_menu = Menu(menu_bar, tearoff=0, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
run_bar = Menu(menu_bar, tearoff=0, bg=BACKGROUND_COLOR, fg=TEXT_COLOR)

compiler.option_add('*TButton*highlightBackground', HIGHLIGHT_COLOR)
compiler.option_add('*TButton*highlightColor', HIGHLIGHT_COLOR)
compiler.option_add('*TButton*background', BACKGROUND_COLOR)
compiler.option_add('*TButton*foreground', TEXT_COLOR)
compiler.option_add('*TButton*borderWidth', 0)

# Other dark mode configurations for menus and labels

# ... (Add similar configurations for other widgets)

compiler.config(menu=menu_bar)

# File Menu
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Exit", command=exit)

# Run Menu
menu_bar.add_cascade(label="Run", menu=run_bar)
run_bar.add_command(label="RUN", command=run)

editor.pack()
code_output.pack()

compiler.mainloop()

