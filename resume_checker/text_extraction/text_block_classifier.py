import re

from text_extraction import library
from utils import regex_utils

def classify(tokens):
    # Getting the weight of each row
    row_weights = []
    for row in tokens:
        row_weights.append(weigh(row))

    print("Row Weights:\n" + str(row_weights) + "\n") # console log

    # Getting NUMBER_OF_SECTION max weight values
    row_weights[0] = -1 # first index should always be -1, first part is most likely personal information
    for index in range(len(row_weights)):
        if row_weights[index] >= 50:
            row_weights[index] = -1
    row_weights.append(-1) # put a default -1 in the end for concatenation purpose

    print("Classified Weights:\n" + str(row_weights) + "\n") # console log

    # Concatenation of rows within blocks
    text_blocks = []
    start_index = 0
    end_index = 0
    while(end_index < len(row_weights) - 1):
        start_index = row_weights.index(-1, end_index)
        end_index = row_weights.index(-1, start_index + 1)
        text_blocks.append(tokens[start_index:end_index])

    # List of List of String to List of String
    for index, block in enumerate(text_blocks):
        text_blocks[index] = " ".join(block)

    return text_blocks

def weigh(row):
    weight = 0
    for section in library.SECTION_TITLES:
        for title in section:
            if (re.search('.*' + regex_utils.add_space_between(title) + '.*', row.lower(), re.DOTALL)):
                weight += len(title.split(' '))
                break

    if (weight == 0):
        return 0

    return  weight / len(row.strip().split(' ')) * 100

def reclassify(categories, text_blocks):
    new_text_blocks = []
    for text_block_category in library.TEXT_BLOCK_CATEGORIES:
        indexes = []
        for category_index, category in enumerate(categories):
            if (text_block_category == category):
                indexes.append(category_index)

        block = ''
        for index in indexes:
            if (block == ''):
                block = text_blocks[index]
            else:
                block += "\n" + text_blocks[index]
        new_text_blocks.append(block)

    return new_text_blocks