# -*- coding: utf-8 -*-
# Reference: https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html

import PyPDF2

need_pip_install = True # If this tool is not installed by the pip, let it be False.
def convert_pdf_to_html(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_html" is used to convert a PDF file to an html file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted html file.
    :return: None
    '''
    # Write your code here
    with open(pdf_file_path, 'rb') as pdf_file:
        # Create a PdfFileReader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Extract text content from the PDF
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Write the extracted text to an HTML file
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write('<!DOCTYPE html>\n<html>\n<body>\n')
        html_file.write(text)
        html_file.write('\n</body>\n</html>')
    
    pass
