import os

file_dir = os.path.dirname(__file__)

# Import extract_text_to_fp function from pdfminer.high_level module
from pdfminer.high_level import extract_text_to_fp

# Import BytesIO class from io module
from io import BytesIO

# Open the PDF file for reading
with open(os.path.join(file_dir, "manuals/adc.pdf"), 'rb') as pdf_file:
    # Create a BytesIO object to store the XML content
    xml_output = BytesIO()

    # Convert the PDF to XML and write it to the BytesIO object
    extract_text_to_fp(pdf_file, xml_output, output_type='xml')

    # Seek to the beginning of the BytesIO object
    xml_output.seek(0)

    # Read the XML content from the BytesIO object
    xml_content = xml_output.read()

# Save the XML content in a file
with open(os.path.join(file_dir, 'output.xml'), 'wb') as output_file:
    output_file.write(xml_content)

# Close the BytesIO object
xml_output.close()