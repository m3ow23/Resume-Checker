import csv

with open("sample.txt", "r", encoding="utf-8") as txt_file:
    lines = txt_file.readlines()

with open("output.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows([line.strip().split(" ") for line in lines])