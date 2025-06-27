import tkinter as tk
from tkinter import ttk
from random import choice
import random

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(window, columns=('First', 'Last', 'Email'), show='headings')
table.heading('First', text='First Name')
table.heading('Last', text='Last Name')
table.heading('Email', text='Email')
table.pack(fill='both', expand=True)

# insert values
# table.insert('', index=0, values=('John', 'Doe', 'johnhoe@gmail.com'))
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first[random.randint(0, len(first) - 1)]}.{last}@gmail.com'
    data = (first, last, email)
    table.insert('', index=0, values=data)


def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])


def delete_items(_):
    print('delete')
    for index in table.selection():
        table.delete(index)


# event
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# items


# run
window.mainloop()
