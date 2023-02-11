from PyPDF2 import PdfReader

# Open the PDF file
pdf_file = open('resume.pdf', 'rb')
pdf_reader = PdfReader(pdf_file)
num_pages = len(pdf_reader.pages)

# Read the PDF content
text = ""
for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Write the text to a file
with open('resume.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(text)