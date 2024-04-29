# -*- coding: utf-8 -*-
# Reference: <FILL IN IF YOU HAVE A REFERENCE>

import os
import pdfplumber
from depdf import *

'''
class CustomDePDF(DePDF):
    @classmethod
    def load(cls, file_name, config=None, **kwargs):
        plumber_pdf = pdfplumber.open(file_name, **kwargs)
        return cls(plumber_pdf, config=config, **kwargs)
    def save_html(self, output_file_path):
        # Your custom implementation here
        # Modify self if necessary
        return super().write_to(output_file_path)
'''

need_pip_install = True

def convert_pdf_to_html(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_html" is used to convert a PDF file to an html file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted html file.
    :return: None
    '''
    # Write your code here
    
    # adopt to_html
    with DePDF.load(pdf_file_path) as pdf:
        html_content = pdf.to_html
    
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    
    '''
    # 效果和第一种采用to_html的一样
    # Load the PDF file
    with CustomDePDF.load(relative_pdf_file_path) as pdf: 
        # Convert PDF to HTML
        # adopt save_html
        pdf.save_html(output_file_path)
    '''

    '''
    # 效果非常不好，整页都是文本信息，没有任何原有的格式
    # Load the PDF file using pdfplumber
    with pdfplumber.open(pdf_file_path) as pdf:
        # Convert PDF to HTML
        html_content = ''
        for page in pdf.pages:
            html_content += page.extract_text()

    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    '''
    pass
