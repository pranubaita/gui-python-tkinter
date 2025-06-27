import tkinter as tk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='lumen')
window.geometry('600x400')
window.title('Menu')

# menu
menu = tk.Menu(window)

# File menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda: print('New File'))
file_menu.add_command(label='Open', command=lambda: print('Open File'))
file_menu.add_separator()
file_menu.add_command(label='Quit', command=window.quit)
menu.add_cascade(label='File', menu=file_menu)

# Help menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='About', command=lambda: print('About'))
help_menu.add_command(label='Help', command=lambda: print('Help'))
help_menu.add_separator()
help_menu_string = tk.BooleanVar()
help_menu.add_checkbutton(label='Advanced Mode', onvalue=True, offvalue=False, variable=help_menu_string, command=lambda: print(help_menu_string.get()))
menu.add_cascade(label='Help', menu=help_menu)

# Edit menu
edit_menu = tk.Menu(menu, tearoff=False)
edit_menu.add_command(label='Cut', command=lambda: print('Cut'))
menu.add_cascade(label='Edit', menu=edit_menu)

edit_options_menu = tk.Menu(menu, tearoff=False)
edit_options_menu.add_command(label='Clear', command=lambda: print('Clear'))
edit_menu.add_cascade(label='Options', menu=edit_options_menu)

# run
window.config(menu=menu)
window.mainloop()
