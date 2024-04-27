# -*- coding: utf-8 -*-
# Reference: https://pypi.org/project/pdftotree/

import pdftotree

def convert_pdf_to_html(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_html" is used to convert a PDF file to an html file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted html file.
    :return: None
    '''
    # Write your code here
    pdftotree.parse(pdf_file_path, output=output_file_path, model_type=None, model_path=None, visualize=False)
    pass
