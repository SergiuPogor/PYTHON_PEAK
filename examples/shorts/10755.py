from contextlib import contextmanager
import zipfile
import os

# context manager to handle opening/closing files safely
@contextmanager
def open_file(file_path, mode):
    file = open(file_path, mode)
    try:
        yield file
    finally:
        file.close()

# context manager to handle unzipping and cleaning up temporary files
@contextmanager
def extract_zip(zip_path, extract_to='/tmp/test/extracted'):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    try:
        yield extract_to
    finally:
        # clean up extracted files after use
        for root, dirs, files in os.walk(extract_to):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))

# Usage Example
zip_path = '/tmp/test/input.zip'
txt_path = '/tmp/test/input.txt'

with open_file(txt_path, 'r') as file:
    print("Reading from file:", file.read())

with extract_zip(zip_path) as extracted_folder:
    print("Files extracted to:", extracted_folder)