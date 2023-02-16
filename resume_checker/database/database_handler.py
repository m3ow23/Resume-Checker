import os
import csv
import shutil

from resume_checker.text_extraction import library

def read():
    file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'r', newline='', encoding='utf-8')
    lines = csv.reader(file)

    database = []
    for line in lines:
        data = line
        if (len(data) != library.NUMBER_OF_SECTIONS - 1 + 2):
            print("Database is corrupted!")
            exit()
        database.append(data)

    return database

def add(id, file_path, final_text_blocks):
    shutil.copy(file_path, os.getcwd() + '\\resume_checker\\database\\resumes\\' + str(get_next_id()))

    if (read() == []):
        file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'w', newline='', encoding='utf-8')
    else:
        file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'a', newline='', encoding='utf-8')

    csvwriter = csv.writer(file)
    csvwriter.writerow([id, file_path] + final_text_blocks[1:])

    file.close()

def clear():
    file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'w')

    file.close()

def get_next_id():
    file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'r', newline='', encoding='utf-8')
    lines = csv.reader(file)

    id = 0
    for index, line in enumerate(lines):
        id += 1
        
    file.close()

    return id

def get_resume(id):
    file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'r', newline='', encoding='utf-8')
    lines = csv.reader(file)

    file_name = ''
    src = 0
    for index, line in enumerate(lines):
        if (id == index):
            file_name = os.path.basename(line[1])
            src = index
            break

    return shutil.copy(os.getcwd() + '\\resume_checker\\database\\resumes\\' + str(src), os.getcwd() + '\\Output Resumes\\' + file_name)