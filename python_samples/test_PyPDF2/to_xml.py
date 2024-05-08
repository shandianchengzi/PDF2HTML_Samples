# -*- coding: utf-8 -*-
# Reference: <FILL IN IF YOU HAVE A REFERENCE>

import PyPDF2
import xml.etree.ElementTree as ET

need_pip_install = True # If this tool is not installed by the pip, let it be False.
def convert_pdf_to_xml(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_xml" is used to convert a PDF file to an xml file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted xml file.
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

    # Convert the extracted text to XML format
    root = ET.Element("PDF_Content")
    text_element = ET.SubElement(root, "Text")
    text_element.text = text

    # Write the XML content to an XML file
    tree = ET.ElementTree(root)
    tree.write(output_file_path)
    pass
