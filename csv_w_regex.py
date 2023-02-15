import csv
import re

# Read the text file
with open("sample.txt", "r", encoding="utf-8") as txt_file:
    resume = txt_file.read()

# Define the patterns to extract the information
name_pattern = re.compile(r'\n^([A-Z][a-z]+\s[A-Z][a-z]+)')
objective_pattern = re.compile(r'Objective\n((?:.*\n)+?)\n')
education_pattern = re.compile(r'Education\n((?:.*\n)+?)\n')
skills_pattern = re.compile(r'Skills\n((?:.*\n)+?)\n')
experience_pattern = re.compile(r'Experience\n((?:.*\n)+?)\n')
certification_pattern = re.compile(r'Certification\n((?:.*\n)+?)\n')
reference_pattern = re.compile(r'Reference\n((?:.*\n)+?)\n')

# Extract the information from the resume
name = re.search(name_pattern, resume)
objective = re.search(objective_pattern, resume)
education = re.search(education_pattern, resume)
skills = re.search(skills_pattern, resume)
experience = re.search(experience_pattern, resume)
certification = re.search(certification_pattern, resume)
reference = re.search(reference_pattern, resume)

# Open the CSV file for writing
with open("output.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file) 
      
    # Write the header row
    writer.writerow(['Name', 'Objective', 'Education', 'Skills', 'Experience', 'Certification', 'Reference'])
    
    # Write the extracted information to the CSV file
    if name and objective and education and skills and experience and certification and reference:
        writer.writerow([name.group(1), objective.group(1), education.group(1), skills.group(1), experience.group(1), 
        certification.group(1), reference.group(1)])
        #writer.writerows([resume.strip().split(" ")])
