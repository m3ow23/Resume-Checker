from database import database_handler
import searcher

database = database_handler.read()
print(database)

qualification_percentage = searcher.get_qualifications(['bachelor'], ['science'], ['instructional'])
print(qualification_percentage)