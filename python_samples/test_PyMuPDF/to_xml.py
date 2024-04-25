# -*- coding: utf-8 -*-
# Reference: <FILL IN IF YOU HAVE A REFERENCE>

import fitz

def convert_pdf_to_xml(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_xml" is used to convert a PDF file to an xml file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted xml file.
    :return: None
    '''
    # Write your code here
    doc = fitz.open(pdf_file_path)
    
    with open(output_file_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        xml_file.write('<pdf>\n')
        
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            xml_file.write(f'<page number="{page_number + 1}">\n')
            xml_file.write('<text>\n')
            
            for text_instance in page.get_text('dict')['blocks']:
                for line in text_instance['lines']:
                    for span in line['spans']:
                        xml_file.write(f'<span font="{span["font"]}" bbox="{span["bbox"]}">{span["text"]}</span>\n')
            
            xml_file.write('</text>\n')
            xml_file.write('</page>\n')
        
        xml_file.write('</pdf>\n')
    pass
