import words
import text_parser
import text_block_classifier
import text_block_categorizer

# check if words.py contents are correct
if ((words.NUMBER_OF_SECTIONS != len(words.SECTION_TITLES))
        or (words.NUMBER_OF_SECTIONS != len(words.TEXT_BLOCK_CATEGORIES))
        or (words.NUMBER_OF_SECTIONS != len(words.WORDS))):
    print('There are unequal number of elements in words.py!')
    exit()

tokens = text_parser.parse('sample.txt')
print('Tokens:\n' + str(tokens) + '\n') # console log

text_blocks = text_block_classifier.classify(tokens)
print('Text Blocks:\n' + str(text_blocks) + '\n') # console log

categories = text_block_categorizer.categorize(text_blocks)
print('Categories:\n' + str(categories) + '\n') # console log