from resume_checker.text_extraction import text_parser
from resume_checker.text_extraction import text_block_classifier
from resume_checker.text_extraction import text_block_categorizer
from resume_checker.database import database_handler

def extract(file_path):
    tokens = text_parser.parse(file_path)
    # console log
    print('>>> TOKENS <<<\n') 
    for row in tokens:
        print(("[" + str(row) + "]").encode('utf-8'))
    print()

    initial_text_blocks = text_block_classifier.classify(tokens)
    # console log
    print('>>> INITIAL TEXT BLOCKS <<<\n')
    for block in initial_text_blocks:
        print(("[" + str(block) + "]").encode('utf-8'))
    print()

    initial_categories = text_block_categorizer.categorize(initial_text_blocks)
    print('>>> INITIAL CATEGORIES <<<\n' + str(initial_categories) + '\n') # console log

    final_text_blocks = text_block_classifier.reclassify(initial_categories, initial_text_blocks)
    # console log
    print('>>> FINAL TEXT BLOCKS <<<\n') 
    for block in final_text_blocks:
        print(("[" + str(block) + "]").encode('utf-8'))
    print()

    print('Extraction Finished')

    database_handler.add(database_handler.get_next_id(), file_path, final_text_blocks)