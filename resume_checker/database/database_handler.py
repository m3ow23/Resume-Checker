import os
import csv

from text_extraction import library

def read():
    file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'r', newline='')
    lines = csv.reader(file)

    database = []
    for line in lines:
        data = line
        if (len(data) != library.NUMBER_OF_SECTIONS):
            print("Database is corrupted!")
            exit()
        database.append(data)

    return database

def add(file_name, final_text_blocks):
    if (read() == []):
        file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'w', newline='')
    else:
        file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'a', newline='')

    csvwriter = csv.writer(file)
    csvwriter.writerow([file_name] + final_text_blocks[1:])

    file.close()

def clear():
    file = open(os.getcwd() + '\\resume_checker\\database\\database.csv', 'w')

    file.close()