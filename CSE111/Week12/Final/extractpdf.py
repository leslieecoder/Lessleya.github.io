import tkinter as tk
from tkinter.constants import BROWSE
import PyPDF2 
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()

# Create the main window. In tkinter,
   
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

    
#logo
logo=Image.open('logo.png')
logo= ImageTk.PhotoImage(logo)
logo_label= tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

# Instructions
directions=tk.Label(root, text='Instructions: Select a PDF file on your computer to extract all its text', font='Raleway')
directions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file","*.pdf")] )
    if file:
        read_pdf= PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)

        #text_box

        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center",1.0,"end")
        text_box.grid(column=1,row=3)

        browse_text.set("Browse")

browse_text=tk.StringVar()
browse_button = tk.Button(root, text="Browse", command=lambda:open_file(), font="Raleway", bg="#FF4E1F", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_button.grid( column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()