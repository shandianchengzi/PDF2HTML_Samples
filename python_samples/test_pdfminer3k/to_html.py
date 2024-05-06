# -*- coding: utf-8 -*-
# Reference: https://www.osgeo.cn/python-tutorial/pdf-pdfminer.html#pdf2txt-py

import subprocess

need_pip_install = False # If this tool is not installed by the pip, let it be False.
def convert_pdf_to_html(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_html" is used to convert a PDF file to an html file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted html file.
    :return: None
    '''
    # Write your code here python_samples\\test_pdfminer\\pdfminer-20191125\\tools\\
    
    try:
        # Call the pdf2txt.py command-line tool to convert PDF to text
        subprocess.run(["python", "python_samples\\test_pdfminer3k\\pdfminer3k-master\\tools\\pdf2txt.py", 
                        "-o", output_file_path, 
                        "-t", "html", 
                        "-s", "1.5", 
                        "-Y", "exact", # exact ：保留每个字符的确切位置（大而混乱的HTML）。
                                       # normal：保留每个文本块中的位置和换行符。（默认）
                                       # loose ：保留每个文本块的整体位置。
                        #"-A",
                        pdf_file_path], check=True)
        print("PDF converted to HTML successfully!")
    except subprocess.CalledProcessError as e:
        print("PDF conversion failed:", e)
    
    pass
