# Reference: https://products.documentprocessing.com/zh/conversion/python/pdfminer.six

# Import BytesIO class from io module
from io import BytesIO

# Import extract_text_to_fp function from pdfminer.high_level module
from pdfminer.high_level import extract_text_to_fp

def convert_pdf_to_html(pdf_file_path, output_file):
    # Create an in-memory buffer to store the HTML output
    output_buffer = BytesIO()

    # Convert the PDF to HTML and write the HTML to the buffer
    with open(pdf_file_path, 'rb') as f:
        extract_text_to_fp(f, output_buffer, output_type='html')

    # Retrieve the HTML content from the buffer
    html_content = output_buffer.getvalue().decode('utf-8')

    # Save the HTML content to the HTML file
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)