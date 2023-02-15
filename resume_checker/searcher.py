import re

from database import database_handler

def get_qualifications(education, experience, skills):
    database = database_handler.read()

    qualifications_percentage = []
    for resume in database:
        for index, text_block in enumerate(resume[1:]):
            weight = 0

            if(index == 0):
                category = education
            elif(index == 1):
                category = experience
            else:
                category = skills

            for word in category:
                if (re.match('.*' + word.lower() + '.*', text_block.lower(), re.DOTALL)):
                    weight += 1
                    continue
        qualifications_percentage.append(weight / len(education + experience + skills) * 100)

    return qualifications_percentage