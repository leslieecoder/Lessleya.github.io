import math 
import tkinter as tk
from PIL import Image, ImageTk

#canva

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=2)

#logo

logo=Image.open('financy.png')
logo= ImageTk.PhotoImage(logo)
logo_label= tk.Label(image=logo)
logo_label.image = logo

logo_label.grid(column=1,row=0)

#instructions

instructions=tk.Label(root, text='Our 50/30/20 calculator divides your take-home income into three categories: 50% for needs, 30% for wants and 20% for savings and debt repayment.', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

instructions.config(font=("Raleway", 10))

directions=tk.Label(root, text='Directions: Enter estimated amounts in all of the fields that apply to you. Round up to the nearest dollar and do not use commas.', font='Raleway')
directions.grid(columnspan=3, column=0, row=2)

directions.config(font=("Raleway", 8))

#Inputs

root.mainloop()