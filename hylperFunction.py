import zipfile
import os

def unzip_files(URL, fileName):
    # Step 1: Download the zip file from GitHub
    os.system(f"wget {URL} -O {fileName}.zip")

    # Step 2: Unzip the file
    with zipfile.ZipFile(f"{fileName}.zip", 'r') as zip_ref:
        zip_ref.extractall()

    print(f"✅ {fileName}.zip downloaded and extracted successfully!")
