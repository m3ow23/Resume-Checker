from tkinter import *
from tkinter import ttk

import searcher
from database import database_handler

def search(my_tree, education, experience, skills):
    qualification_percentage = searcher.get_qualifications(education, experience, skills)
    my_tree.delete(*my_tree.get_children())
    for i, resume in enumerate(qualification_percentage):
        my_tree.insert('', index='end', iid=i + 1, text=i + 1, values=(resume[0], resume[1]))

    print("Searched Database")

def open_file():
    print("Button Clicked") 

def clear():
    database_handler.clear()
    print("Database has been cleared")

def show():
    window = Tk()

    window.geometry("800x500")
    window.configure(bg="#2c3333")
    canvas = Canvas(
        window,
        bg="#2c3333",
        height=500,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    background="#E7F6F2",
                    rowheight=25,
                    fieldbackground="#E7F6F2")
    my_tree = ttk.Treeview()
    my_tree['columns'] = ("File Name", "Qualification")

    my_tree.column("#0", width=30, minwidth=25)
    my_tree.column("File Name", width=100, anchor=W)
    my_tree.column("Qualification", anchor=CENTER, width=100)

    # Headings
    my_tree.heading("#0", text="#", anchor=CENTER)
    my_tree.heading("File Name", text="File Name", anchor=CENTER)
    my_tree.heading("Qualification", text="Qualification", anchor=CENTER)

    my_tree.place(x=447, y=70, width=319, heigh=281)

    img0 = PhotoImage(file="resume_checker\\gui\\img0.png")
    btnOpen = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=open_file,
        relief="flat")

    btnOpen.place(
        x=34, y=27,
        width=190,
        height=43)

    lblFile = Label(
        font=("Archivo Black", 15, "bold"),
        bg="#2c3333",
        fg="white",
        text="File Path:"
    )

    lblFile.place(
        x=240,
        y=30
    )

    education = ['bachelor']
    experience = ['science']
    skills = ['instructional']

    imgSearch = PhotoImage(file="resume_checker\\gui\\imgSearch.png")
    btnSearch = Button(
        image=imgSearch,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: search(my_tree, education, experience, skills),
        relief="flat")

    btnSearch.place(
        x=129, y=367,
        width=190,
        height=43)

    imgClear = PhotoImage(file="resume_checker\\gui\\imgClear.png")
    btnClear = Button(
        image=imgClear,
        borderwidth=0,
        highlightthickness=0,
        command=clear,
        relief="flat")

    btnClear.place(
        x=512, y=367,
        width=190,
        height=43)


    window.resizable(False, False)
    window.mainloop()