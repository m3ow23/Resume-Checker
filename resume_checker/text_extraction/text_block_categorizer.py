import re

from resume_checker.text_extraction import library
from resume_checker.utils import regex_utils

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
        if (re.search('.*' + regex_utils.add_space_between(word) + '.*', block.lower(), re.DOTALL)):
            weight += len(word.split(' '))
    return weight