from tkinter import * 
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter.font import Font
from tkinter.scrolledtext import*
import file_menu
import edit_menu
import format_menu
import help_menu

#Create tkinter window
root=Tk()

#title and dimensions
root.title("Alexis Kay notepad clone")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

#something
text = ScrolledText(root, state='normal', height=400, width=400, wrap ='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

#menubar
menuBar = Menu(root)
file_menu.main(root, text, menuBar)
edit_menu.main(root, text, menuBar)
format_menu.main(root, text, menuBar)
help_menu.main(root, text, menuBar)

#runit
root.mainloop()