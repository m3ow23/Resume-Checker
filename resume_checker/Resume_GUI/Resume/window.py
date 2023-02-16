from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PyPDF2 import PdfReader
import docx2txt
import os


def btn_clicked():
    print("Button Clicked")

# ---------- FUNCTION TO OPEN FILE ---------- #
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\", filetypes=(("text files", "*.txt"),
                                          ("PDF files", "*.pdf"), ("Word Files", "*.docx")))
    filename = os.path.basename(filepath)
    lblPath = Label(
        font=("Archivo Black", 15, "bold"),
        bg="#2c3333",
        fg="white",
        text=filename
    )

    lblPath.place(
        x=340,
        y=30
    )

    if filepath.endswith('.pdf'):
        file = open(filepath, 'rb')
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Read the PDF content
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        # Close the PDF file
        file.close()

        # Write the text to a file
        with open('resumesample.txt', 'w', encoding='utf-8') as text_file:
            text_file.write(text)

    elif filepath.endswith('.docx'):
        # Replace 'document.docx' with the path to your Word document
        text = docx2txt.process(filepath)

        # Print the extracted text
        with open('resumesample1.txt', 'w', encoding='utf-8') as text_file:
            text_file.write(text)

    else:
        print("Error")

window = Tk()

window.geometry("800x500")
window.configure(bg = "#2c3333")
canvas = Canvas(
    window,
    bg = "#2c3333",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# ---------- TREEVIEW ---------- #
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#E7F6F2",
                rowheight=25,
                fieldbackground="#E7F6F2")

tree_frame = Frame(window)
tree_frame.pack(pady=20)

# Scroll
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

my_tree.place(width=305, heigh=281)
tree_frame.place(x=447, y=70, width=319, heigh=281)

# Treeview Columns
my_tree['columns'] = ("File Name", "Qualification")

my_tree.column("#0", width=30, minwidth=25)
my_tree.column("File Name", width=100, anchor=W)
my_tree.column("Qualification", anchor=CENTER, width=100)

# Headings
my_tree.heading("#0", text="#", anchor=CENTER)
my_tree.heading("File Name", text="File Name", anchor=CENTER)
my_tree.heading("Qualification", text="Qualification", anchor=CENTER)

# Insert rows
my_tree.insert(parent='', index='end', iid=0, text="1", values=("Resume", "50%"))

# ---------- BUTTONS ---------- #
# Open File
img0 = PhotoImage(file = "img0.png")
btnOpen = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = openFile,
    relief = "flat")

btnOpen.place(
    x = 34, y = 27,
    width = 190,
    height = 43)

# Search
imgSearch = PhotoImage(file = "imgSearch.png")
btnSearch = Button(
    image = imgSearch,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btnSearch.place(
    x = 129, y = 367,
    width = 190,
    height = 43)

# Clear Table
imgClear = PhotoImage(file = "imgClear.png")
btnClear = Button(
    image = imgClear,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btnClear.place(
    x = 512, y = 367,
    width = 190,
    height = 43)

# ---------- LABELS ---------- #
lblFile = Label(
    font=("Archivo Black",15, "bold"),
    bg="#2c3333",
    fg="white",
    text="File Path:"
)

lblFile.place(
    x=240,
    y=30
)

label1 = Label(
    window,
    text="Education\n\n\nExperience\n\n\nSkills\n\n\nLanguage",
    font="Times 14",
    bg="#2c3333",
    fg="white"
)

label1 = Label(window, text = "Education\n\n\nExperience\n\n\nSkills\n\n\nLanguage",
               font="Times 14",
               bg = "#2c3333",
               fg = "white",
               justify = "left")
label1.pack()

label1.place(
    x = 0, y = 100,
    width = 190,
    height = 220)

# ---------- ENTRIES ---------- #
education = Entry(window,
                  width=25,
                  font = "Times 14",
                  bg = "#E7F6F2")
education.place(x=170, y=105)

experience = Entry(window,
                   width=25,
                   font = "Times 14",
                   bg = "#E7F6F2")
experience.place(x=170, y=170)

skills = Entry(window,
               width=25,
               font = "Times 14",
               bg = "#E7F6F2")
skills.place(x=170, y=230)

language = Entry(window,
                 width=25,
                 font = "Times 14",
                 bg = "#E7F6F2")
language.place(x=170, y=295)

window.resizable(False, False)
window.mainloop()
