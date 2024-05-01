# -*- coding: utf-8 -*-
# Reference: <FILL IN IF YOU HAVE A REFERENCE>

import xml.etree.ElementTree as ET
from poppdf.pdf import * 

need_pip_install = True # If this tool is not installed by the pip, let it be False.
def convert_pdf_to_xml(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_xml" is used to convert a PDF file to an xml file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted xml file.
    :return: None
    '''
    # Write your code here
    # Convert the extracted text to XML
    xml_data = xml_from_path(pdf_file_path)
    xml_string = ET.tostring(xml_data, encoding='utf-8', method='xml').decode()

    # Write the XML data to the output file
    with open(output_file_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_string)
    pass