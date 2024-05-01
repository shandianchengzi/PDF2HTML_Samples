# -*- coding: utf-8 -*-
# Reference: https://pypi.org/project/poppdf/

from poppdf.pdfDocument import PdfDocument

need_pip_install = True # If this tool is not installed by the pip, let it be False.
def convert_pdf_to_html(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_html" is used to convert a PDF file to an html file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted html file.
    :return: None
    '''
    # Write your code here
    pdf = PdfDocument(pdf_file_path)
    
    html_content = ""
    for page in pdf.pdf_pages:
        html_content += page.text

    # Write HTML content to file
    with open(output_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    pass
