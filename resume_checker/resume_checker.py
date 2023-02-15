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
# console log
print('>>> TOKENS <<<\n') 
for row in tokens:
    print("[" + str(row) + "]")
print()

initial_text_blocks = text_block_classifier.classify(tokens)
# console log
print('>>> INITIAL TEXT BLOCKS <<<\n')
for block in initial_text_blocks:
    print("[" + str(block) + "]")
print()

initial_categories = text_block_categorizer.categorize(initial_text_blocks)
print('>>> INITIAL CATEGORIES <<<\n' + str(initial_categories) + '\n') # console log

final_text_blocks = text_block_classifier.reclassify(initial_categories, initial_text_blocks)
# console log
print('>>> FINAL TEXT BLOCKS <<<\n') 
for block in final_text_blocks:
    print("[" + str(block) + "]")
print()

final_categories = text_block_categorizer.categorize(final_text_blocks)
print('>>> FINAL CATEGORIES <<<\n' + str(final_categories) + '\n') # console log