# from database import database_handler
# import searcher

# database = database_handler.read()
# print(database)

# qualification_percentage = searcher.get_qualifications(['bachelor'], ['science'], ['instructional'])
# print(qualification_percentage)
import re
from resume_checker.utils import regex_utils
word = 'education'

print(regex_utils.add_space_between(word), re.match('.*' + regex_utils.add_space_between(word) + '.*', 'ed    u ca    tion', re.DOTALL))