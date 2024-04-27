# -*- coding: utf-8 -*-
# Reference: https://blog.csdn.net/eiceblue/article/details/135988859
# https://www.e-iceblue.cn/pdf_python_conversion/python-convert-pdf-to-html.html

from spire.pdf.common import *
from spire.pdf import *

def convert_pdf_to_html(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_html" is used to convert a PDF file to an html file.
    :param pdf_file_path: str: The file path of the PDF file to be converted.
    :param output_file_path: str: The file path to save the converted html file.
    :return: None
    '''
    # Write your code here
    # Create an instance of PdfDocument class
    doc = PdfDocument()

    # Load a PDF document
    doc.LoadFromFile(pdf_file_path)

    # Options->https://blog.csdn.net/eiceblue/article/details/135988859
    pdfToHtmlOptions = doc.ConvertOptions
    pdfToHtmlOptions.SetPdfToHtmlOptions(True, True, 10, True)

    # Convert the document to HTML
    doc.SaveToFile(output_file_path, FileFormat.HTML)
    doc.Close()

    pass
