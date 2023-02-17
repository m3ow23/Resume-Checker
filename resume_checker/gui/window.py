from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import threading

from resume_checker.text_extraction import text_extractor
from resume_checker import searcher
from resume_checker.database import database_handler

# ---------- FUNCTION TO OPEN FILE ---------- #
def open_file(lblPath):
    print('Open File Button Clicked')
    file_path = filedialog.askopenfilename(initialdir="C:\\", filetype=([("Resume Files", "*.txt *.pdf *.docx")]))
    if (not file_path):
        print('No Input Selected')
        return
    
    lblPath.config(text='processing file...')    

    thread = threading.Thread(target=process_file_thread, args=(file_path, lblPath))
    thread.start()

def process_file_thread(file_path, lblPath):
    # Process the file
    text_extractor.extract(file_path)
    # Update the label to show the file name
    lblPath.config(text=os.path.basename(file_path))

def search(my_tree, education, experience, skills):
    print('Search Button Clicked')
    qualification_percentage = searcher.get_qualifications(education, experience, skills)
    sorted_qualification_percentage = sorted(qualification_percentage, key=lambda x: x[1], reverse=True)
    my_tree.delete(*my_tree.get_children())
    for i, resume in enumerate(sorted_qualification_percentage):
        my_tree.insert('', index='end', iid=resume[2] + 1, text=resume[2] + 1, values=((os.path.basename(resume[0]), str(resume[1]) + '%')))

def clear_tree(my_tree):
    my_tree.delete(*my_tree.get_children())
    database_handler.clear()

    # Clear database\resumes
    folder_path = os.getcwd() + '\\resume_checker\\database\\resumes'
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Clear Output Resumes
    folder_path = os.getcwd() + '\\Output Resumes'
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

def clear_text_boxes(education, experience, skills, language):
    education.delete(0, END)
    experience.delete(0, END)
    skills.delete(0, END)
    language.delete(0, END)

def clear_everything(my_tree, education, experience, skills, language, lblPath):
    print("Text boxes and Database are cleared")
    clear_text_boxes(education, experience, skills, language)
    clear_tree(my_tree)

    lblPath.config(text='')

def table_item_select(event, my_tree):
    item = my_tree.selection()[0]
    if (item):
        file_path = database_handler.get_resume(int(item) - 1)
        print('Opening File: ' + file_path)
        subprocess.Popen(['start', '', file_path], shell = True)

def show():
    window = Tk()
    window.title('Resume Checker')

    window.geometry("800x500")
    window.configure(bg = "#2c3333")
    canvas = tk.Canvas(
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

    my_tree.bind("<<TreeviewSelect>>", lambda event: table_item_select(event, my_tree))

    # ---------- BUTTONS ---------- #
    # Open File
    img0 = PhotoImage(file = "resume_checker\\gui\\img0.png")
    btnOpen = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: open_file(lblPath),
        relief = "flat")

    btnOpen.place(
        x = 34, y = 27,
        width = 190,
        height = 43)

    # Search
    imgSearch = PhotoImage(file = "resume_checker\\gui\\imgSearch.png")
    btnSearch = Button(
        image = imgSearch,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: search(my_tree, education.get(), experience.get(), skills.get() + ',' + language.get()),
        relief = "flat")

    btnSearch.place(
        x = 129, y = 367,
        width = 190,
        height = 43)

    # Clear Table
    imgClear = PhotoImage(file = "resume_checker\\gui\\imgClear.png")
    btnClear = Button(
        image = imgClear,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: clear_everything(my_tree, education, experience, skills, language, lblPath),
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
        text="File Name:"
    )

    lblFile.place(
        x=240,
        y=30
    )

    lblPath = Label(
        font=("Archivo Black", 15, "bold"),
        bg="#2c3333",
        fg="white",
        text=""
    )

    lblPath.place(
        x=350,
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
