from tkinter import *
from tkinter.messagebox import*

class Help():
    def about(root):
        showinfo(title="About", message=" Simple little text editor made by Alexis Kay ")
    
def main(root, text, menuBar):
    help = Help()

    helpMenu = Menu(menuBar)
    helpMenu.add_command(label="About", command=help.about)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menuBar)

if __name__ == "__main":
    print("run Main.py")

