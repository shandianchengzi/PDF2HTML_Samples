# -*- coding: utf-8 -*-
# Reference: https://www.freecodecamp.org/chinese/news/extract-data-from-pdf-files-with-python

import pandas as pd
import pdfquery

def convert_pdf_to_xml(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_xml" is used to convert a PDF file to an xml file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted xml file.
    :return: None
    '''
    # Write your code here

    # Read PDF
    pdf = pdfquery.PDFQuery(pdf_file_path)
    pdf.load()

    # Convert PDF to XML
    pdf.tree.write(output_file_path, pretty_print = True)
    pdf
    pass
