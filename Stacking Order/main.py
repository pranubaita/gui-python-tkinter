import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename='lumen')
window.geometry('400x400')
window.title('Stacking Order')

# widgets
label1 = ttk.Label(window, text='Label 1', background='green')
label2 = ttk.Label(window, text='Label 2', background='red')
label3 = ttk.Label(window, text='Label 3', background='blue')

button1 = ttk.Button(window, text='Raise Button 1', command=lambda: label1.tkraise())
button2 = ttk.Button(window, text='Raise Button 2', command=lambda: label2.tkraise())
button3 = ttk.Button(window, text='Raise Button 3', command=lambda: label3.tkraise())

# layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=20, y=90, width=190, height=75)

button1.place(relx=0.4, rely=1, anchor='se')
button2.place(relx=0.7, rely=1, anchor='se')
button3.place(relx=1, rely=1, anchor='se')

# run
window.mainloop()
