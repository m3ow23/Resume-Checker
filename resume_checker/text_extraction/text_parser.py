from PyPDF2 import PdfReader
import docx2txt

def parse(file_path):
    tokens = []

    # pdf file parser
    if file_path.endswith('.pdf'):
        file = open(file_path, 'rb')
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            lines = text.splitlines(keepends=True)
            tokens += lines

        file.close()

    # docx file parser
    elif file_path.endswith('.docx'):
        tokens = docx2txt.process(file_path).splitlines(keepends=True)

    # read text file
    elif file_path.endswith('.txt'):
        file = open(file_path, encoding='utf-8').readlines()

        for line in file:
            tokens.append(line)

    else:
        print("Invalid File Type!")

    return tokens