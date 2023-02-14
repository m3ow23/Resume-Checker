from text_extraction import library
from text_extraction import text_parser
from text_extraction import text_block_classifier
from text_extraction import text_block_categorizer
from text_extraction import named_entity_classifier

# check if library.py contents are correct
if ((library.NUMBER_OF_SECTIONS != len(library.SECTION_TITLES))
        or (library.NUMBER_OF_SECTIONS != len(library.TEXT_BLOCK_CATEGORIES))
        or (library.NUMBER_OF_SECTIONS != len(library.WORDS))):
    print('There are unequal number of elements in library.py!')
    exit()

print('Enter file name: ')
file = input()

tokens = text_parser.parse('resume_checker\\' + str(file))
print('Tokens:\n' + str(tokens) + '\n') # console log

text_blocks = text_block_classifier.classify(tokens)
print('Initial Text Blocks:\n' + str(text_blocks) + '\n') # console log

categories = text_block_categorizer.categorize(text_blocks)
print('Initial Categories:\n' + str(categories) + '\n') # console log

text_blocks = text_block_classifier.reclassify(categories, text_blocks)
print('Final Text Blocks:\n' + str(text_blocks) + '\n') # console log

categories = text_block_categorizer.categorize(text_blocks)
print('Final Categories:\n' + str(categories) + '\n') # console log

named_entities = named_entity_classifier.classify(text_blocks)
print('Named Entities:\n' + str(named_entities) + '\n') # console log