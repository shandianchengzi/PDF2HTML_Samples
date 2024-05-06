# -*- coding: utf-8 -*-
# Reference: <FILL IN IF YOU HAVE A REFERENCE>

import subprocess

need_pip_install = False # If this tool is not installed by the pip, let it be False.
def convert_pdf_to_xml(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_xml" is used to convert a PDF file to an xml file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted xml file.
    :return: None
    '''
    # Write your code here
    # Execute pdftohtml command
    try:
        subprocess.run(["pdftohtml", "-xml", pdf_file_path, output_file_path])
        print("PDF converted to XML successfully!")
    except FileNotFoundError:
        print("pdftohtml command not found. Make sure poppler is installed and added to your system PATH.")
    pass
