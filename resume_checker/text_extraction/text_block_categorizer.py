import re

from text_extraction import library

def categorize(text_blocks):
    categories = [None]*len(text_blocks)
    for index, block in enumerate(text_blocks):
        category_weights = [0]*library.NUMBER_OF_SECTIONS
        for category_index, category_words in enumerate(library.WORDS):
            category_weights[category_index] = weigh(block, category_words)
        categories[index] = library.TEXT_BLOCK_CATEGORIES[category_weights.index(max(category_weights))]
    return categories

def weigh(block, category_words):
    weight = 0
    for word in category_words:
        if (re.search(word, block.lower())):
            weight += len(word.split(' '))
    return weight