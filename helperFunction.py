import requests
from zipfile import ZipFile
from io import BytesIO
import os

def download_and_extract_zip(url, extract_to="dataset"):
    """
    Downloads a ZIP file from a URL and extracts it to a folder.

    Parameters:
    - url: str, URL of the ZIP file
    - extract_to: str, folder name to extract files into
    """
    # Create folder if it doesn't exist
    os.makedirs(extract_to, exist_ok=True)

    print(f"Downloading from: {url}")
    response = requests.get(url)
    response.raise_for_status()  # Raises error if download fails

    # Open the ZIP from memory and extract
    with ZipFile(BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(extract_to)

    print(f"Files extracted to: {extract_to}")
    return os.listdir(extract_to)


# import zipfile
# import os

# def unzip_files(URL, fileName):
#     # Step 1: Download the zip file from GitHub
#     os.system(f"wget {URL} -O {fileName}.zip")

#     # Step 2: Unzip the file
#     with zipfile.ZipFile(f"{fileName}.zip", 'r') as zip_ref:
#         zip_ref.extractall()

#     print(f"✅ {fileName}.zip downloaded and extracted successfully!")
