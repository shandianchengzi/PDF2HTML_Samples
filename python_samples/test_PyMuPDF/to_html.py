# -*- coding: utf-8 -*-
# Reference: https://blog.csdn.net/qq_28505809/article/details/124147552

import fitz
from tqdm import tqdm

def convert_pdf_to_html(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_html" is used to convert a PDF file to an html file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted html file.
    :return: None
    '''
    # Write your code here
    doc = fitz.open(pdf_file_path)
    print(doc)
    html_content = "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><title>Title</title></head><body style=\"display: flex;justify-content: center;flex-direction: column;background: white;align-items: center;\">"
    for page in tqdm(doc):
        html_content += page.get_text('html')
    print("开始输出html文件")
 
    html_content += "</body></html>"
    with open(output_file_path, 'w', encoding='utf8', newline="") as fp:
        fp.write(html_content)
 
    pass