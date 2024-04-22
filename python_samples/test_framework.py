###################################################################
#-------------------   Don't Need to Change ----------------------#
###################################################################

import os

def test_func(func):
    # get the dirname of func
    file_dir = os.path.dirname(func.__code__.co_filename)
    file_name = os.path.basename(func.__code__.co_filename)

    pdf_files_path = os.path.join(file_dir, "../../input_pdf")
    pdf_files = os.listdir(pdf_files_path)

    # mkdir outputs
    os.makedirs(os.path.join(file_dir, "outputs"), exist_ok=True)
    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(pdf_files_path, pdf_file)
        output_file_path = os.path.join(file_dir, "outputs", file_name.split(".")[0] + '_' + pdf_file.replace(".pdf", ".html"))
        func(pdf_file_path, output_file_path)
        # Print a message indicating where the HTML file is saved
        print(f'Output saved to {output_file_path}')