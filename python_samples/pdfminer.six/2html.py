# Import extract_text_to_fp function from pdfminer.high_level module
from pdfminer.high_level import extract_text_to_fp

# Import BytesIO class from io module
from io import BytesIO

import os

file_dir = os.path.dirname(__file__)

# Specify the PDF file you want to convert to HTML
pdf_file = os.path.join(file_dir, 'input.pdf')

# Create an in-memory buffer to store the HTML output
output_buffer = BytesIO()

# Convert the PDF to HTML and write the HTML to the buffer
with open(pdf_file, 'rb') as pdf_file:
    extract_text_to_fp(pdf_file, output_buffer, output_type='html')

# Retrieve the HTML content from the buffer
html_content = output_buffer.getvalue().decode('utf-8')

# Specify the HTML file where you want to save the content
html_output_file = os.path.join(file_dir, 'output.html')

# Save the HTML content to the HTML file
with open(html_output_file, 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

# Print a message indicating where the HTML file is saved
print(f'HTML content saved to {html_output_file}')