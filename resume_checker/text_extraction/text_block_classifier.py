from text_extraction import words

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
        text_block = build_block(tokens[start_index:end_index])
        text_blocks.append(text_block)

    return text_blocks

def weigh(row):
    weight = 0
    for token in row:
        for section in words.SECTION_TITLES:
            if (token in section):
                weight += 1
                break

    if (weight == 0):
        return 0
    return  weight / len(row) * 100

def build_block(rows):
    text_block = []
    for token in rows:
        text_block += token

    return text_block

def reclassify(categories, text_blocks):
    for index_a, category_a in enumerate(categories):
        for index_b, category_b in enumerate(categories):
            if (index_a == index_b or category_a == -1 or category_b == -1):
                break
            if (category_a == category_b):
                text_blocks[index_b] = build_block([text_blocks[index_b], text_blocks[index_a]])
                text_blocks.remove(text_blocks[index_a])
                category_a = -1
    
    return text_blocks