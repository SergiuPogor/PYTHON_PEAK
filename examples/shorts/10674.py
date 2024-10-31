from contextlib import closing
import zipfile

def extract_zip(file_path, extract_to):
    # Opening a zip file object that doesn't have native context manager support
    with closing(zipfile.ZipFile(file_path, 'r')) as zip_file:
        zip_file.extractall(extract_to)

# Usage example
try:
    extract_zip('/tmp/test/input.zip', '/tmp/test/extracted')
    print("Files extracted successfully.")
except Exception as e:
    print("An error occurred:", e)
    
# This method is especially useful for files or sockets that don't natively support
# context managers but still need to be closed reliably.