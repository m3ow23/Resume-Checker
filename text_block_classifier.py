import words

def classify(tokens):
    # Getting the weight of each row
    row_weights = []
    for row_index, row in enumerate(tokens):
        row_weights.append(weigh(row))

    print("Row Weights:\n" + str(row_weights) + "\n") # console log

    # Getting NUMBER_OF_SECTION max weight values
    for i in range(words.NUMBER_OF_SECTIONS):
        row_weights[row_weights.index(max(row_weights))] = -1
    row_weights.append(-1) # put a default -1 in the end for concatenation purpose

    print("Classified Weights:\n" + str(row_weights) + "\n") # console log

    # Concatenation of rows within blocks
    text_blocks = []
    start_index = 0
    end_index = 0
    for i in range(words.NUMBER_OF_SECTIONS):
        start_index = row_weights.index(-1, end_index)
        end_index = row_weights.index(-1, start_index + 1) - 1
        text_block = build_block(tokens[start_index:end_index])
        text_blocks.append(text_block)

    return text_blocks

def weigh(row):
    weight = 0
    for token in row:
        if (token in words.SECTION_TITLES):
            weight += 1

    if (weight == 0):
        return 0
    return  weight / len(row) * 100

def build_block(rows):
    text_block = []
    for token in rows:
        text_block += token

    return text_block