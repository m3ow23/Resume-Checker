import re

from text_extraction import library

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
            if (re.search(title, row.lower())):
                weight += len(title.split(' '))
                break

    if (weight == 0):
        return 0

    return  weight / len(row.split(' ')) * 100

def build_block(rows):
    text_block = []
    for row in rows:
        text_block += row

    return text_block

def reclassify(categories, text_blocks):
    for index_a, category_a in enumerate(categories):
        for index_b, category_b in enumerate(categories):
            if (index_a == index_b or category_a == -1 or category_b == -1):
                break
            if (category_a == category_b):
                text_blocks[index_b] = text_blocks[index_b] + text_blocks[index_a]
                text_blocks.remove(text_blocks[index_a])
                category_a = -1
    
    return text_blocks