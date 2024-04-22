# Reference: https://products.documentprocessing.com/zh/conversion/python/pdfminer.six

# Import extract_text_to_fp function from pdfminer.high_level module
from pdfminer.high_level import extract_text_to_fp

# Import BytesIO class from io module
from io import BytesIO

def convert_pdf_to_xml(pdf_file_path, output_file_path):
    '''
    "convert_pdf_to_xml" is used to convert a PDF file to an HTML file.
    :param pdf_file_path: The path to the PDF file to be converted.
    :param output_file_path: The path to save the converted HTML file.
    :return: None
    '''

    # Open the PDF file for reading
    with open(pdf_file_path, 'rb') as pdf_file:
        # Create a BytesIO object to store the XML content
        xml_output = BytesIO()

        # Convert the PDF to XML and write it to the BytesIO object
        extract_text_to_fp(pdf_file, xml_output, output_type='xml')

        # Seek to the beginning of the BytesIO object
        xml_output.seek(0)

        # Read the XML content from the BytesIO object
        xml_content = xml_output.read()

    # Save the XML content in a file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(xml_content)

    # Close the BytesIO object
    xml_output.close()
    pass
