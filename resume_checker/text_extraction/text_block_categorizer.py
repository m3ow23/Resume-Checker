from text_extraction import words

def categorize(text_blocks):
    categories = [None]*len(text_blocks)
    for index, text_block in enumerate(text_blocks):
        category_weights = [0]*words.NUMBER_OF_SECTIONS
        for category_index, category_words in enumerate(words.WORDS):
            category_weights[category_index] = weigh(text_block, category_words)
        categories[index] = words.TEXT_BLOCK_CATEGORIES[category_weights.index(max(category_weights))]
    return categories

def weigh(text_block, category_words):
    weight = 0
    for token in text_block:
        if token in category_words:
            weight += 1
    return weight