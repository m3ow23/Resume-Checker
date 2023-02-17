# from database import database_handler
# import searcher

# database = database_handler.read()
# print(database)

# qualification_percentage = searcher.get_qualifications(['bachelor'], ['science'], ['instructional'])
# print(qualification_percentage)
import re
from utils import regex_utils
row = '             s k i l l s  s e t'

if (re.match('.*[^ ] . [^ ].*', row)):
    sub_double_space = re.sub('  ', '!@#$%^&*', row)
    remove_single_space = sub_double_space.replace(' ', '')
    row = remove_single_space.replace('!@#$%^&*', ' ')
    row = row.strip()
    print(row)