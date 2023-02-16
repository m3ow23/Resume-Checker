import re

from resume_checker.database import database_handler
from resume_checker.utils import regex_utils

def get_qualifications(education, experience, skills):
    database = database_handler.read()

    education = [word.strip().lower() for word in education.split(',')]
    experience = [word.strip().lower() for word in experience.split(',')]
    skills = [word.strip().lower() for word in skills.split(',')]

    print(education, experience, skills)

    qualifications_percentage = []
    for resume in database:
        weight = 0
        for index, text_block in enumerate(resume[2:]):

            if(index == 0):
                category = education
            elif(index == 1):
                category = experience
            else:
                category = skills

            for word in category:
                if (not word):
                    continue
                if (re.match('.*' + regex_utils.add_space_between(word) + '.*', text_block.lower(), re.DOTALL)):
                    weight += 1
                    continue
        
        total = len([element for element in education + experience + skills if element])

        if (total == 0):
            qualifications_percentage.append([resume[1], 100])
        else:
            qualifications_percentage.append([resume[1], round(weight / total * 100)])

    print(qualifications_percentage)
    return qualifications_percentage