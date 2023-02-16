from resume_checker.gui import window
from resume_checker.text_extraction import library

# check if library.py contents are correct
if ((library.NUMBER_OF_SECTIONS != len(library.SECTION_TITLES))
        or (library.NUMBER_OF_SECTIONS != len(library.TEXT_BLOCK_CATEGORIES))
        or (library.NUMBER_OF_SECTIONS != len(library.WORDS))):
    print('There are unequal number of elements in library.py!')
    exit()

window.show()