import text_block_classifier
import text_parser

tokens = text_parser.parse('sample.txt')
print("Tokens:\n" + str(tokens) + "\n") # console log

text_blocks = text_block_classifier.classify(tokens)
print("Text Blocks:\n" + str(text_blocks) + "\n") # console log