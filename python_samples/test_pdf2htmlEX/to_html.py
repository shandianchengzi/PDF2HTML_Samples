import subprocess
import os

need_pip_install = False

file_dir = os.path.dirname(os.path.abspath(__file__))

def convert_pdf_to_html(pdf_file_path, output_file_path):
    """
    Convert a PDF file to an HTML file using pdf2htmlEX.

    :param pdf_file_path: str: The absolute file path of the PDF file to be converted.
    :param output_file_path: str: The absolute file path to save the converted HTML file.
    :return: bool: True if conversion is successful, False otherwise.
    """
    # pdf2htmlEX 所在文件夹
    exe_file_path = os.path.join(file_dir, "pdf2htmlEX")
    # Change to the target directory
    os.chdir(exe_file_path)
    if not os.path.exists(exe_file_path):
        print("Error: pdf2htmlEX executable not found.")
        return False
    
    relative_output_path = os.path.relpath(output_file_path, os.path.dirname(exe_file_path))
    relative_output_path = os.path.join("..", relative_output_path)
    # Construct the command
    # More Command Line Options：https://github.com/coolwanglu/pdf2htmlEX/wiki/Command-Line-Options
    command = [
        "pdf2htmlex",
        "--optimize-text", "1",
        "--zoom", "1.5",
        "--process-outline", "1",
        "--font-format", "woff",
        pdf_file_path,
        relative_output_path
    ]

    # Execute the command
    try:
        print("Command:", " ".join(command))
        subprocess.run(command, check=True)
        print("Conversion successful. Output saved to", output_file_path)
        return True
    except subprocess.CalledProcessError as e:
        print("Error when Command {}".format({" ".join(command)}))
        return False