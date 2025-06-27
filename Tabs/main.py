import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename='superhero')
window.title('Tabs')
window.geometry('700x500')

# Notebook widget
notebook = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(notebook, width=200, height=200)
Tab1Clicked = tk.StringVar()
Tab2Clicked = tk.StringVar()
label = ttk.Label(tab1, textvariable=Tab1Clicked, padding=10)
button = ttk.Button(tab1, text='A Sample Button', command=lambda: Tab1Clicked.set('WOW!'))
label3 = ttk.Label(tab1, textvariable=Tab2Clicked, padding=10)
label.pack()
button.pack()
label3.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='Another Text in Another Tab', padding=10)
entry = ttk.Entry(tab2, textvariable=Tab2Clicked)
empty = ttk.Label(tab2, font='Helvetica 4 bold')
button2 = ttk.Button(tab2, text='See you at Tab 1!', command=lambda: Tab2Clicked.set(entry.get()))
label2.pack()
entry.pack()
empty.pack()
button2.pack()

# Tab 3
tab3 = ttk.Frame(notebook)
button3 = ttk.Button(tab3, text='LOL')
button4 = ttk.Button(tab3, text='DOUBLE LOL')
label4 = ttk.Label(tab3, text='so many labels', padding=10)
button3.pack()
button4.pack()
label4.pack()

# Notebook initialization
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')
notebook.pack()

# run
window.mainloop()
