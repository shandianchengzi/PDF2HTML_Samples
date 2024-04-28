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
    pdftotree.parse(pdf_file_path, output_file_path, visualize = False)

    '''
     # Parse PDF without visualization
    pdftotree.parse(pdf_file_path, output_file_path)
    
    # Read HTML file and add CSS for visualization
    with open(output_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    
    # Add CSS for visualization
    html_content = f'<style>body{{max-width: 600px;}}</style>\n{html_content}'
    
    # Write modified HTML content back to file
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    '''

    pass
