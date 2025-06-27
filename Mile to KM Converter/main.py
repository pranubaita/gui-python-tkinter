import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


# commands
def convert():
    mile_input = entryIntVar.get()
    km_output = round(mile_input * 1.61, 2)
    output_string.set(str(km_output))


# window
window = ttk.Window(themename='superhero')
window.title('Mile to KM Converter')
window.geometry('300x150')
# label
title_label = ttk.Label(master=window, text='Miles to Kilometers', font=('Barlow Condensed', 24))
title_label.pack()
# input
input_frame = ttk.Frame(master=window)
entryIntVar = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryIntVar)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left')
button.pack(side='left', padx=3)
input_frame.pack(pady=10)
# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Calibri 20', textvariable=output_string)
output_label.pack(pady=5)
# run
window.mainloop()
