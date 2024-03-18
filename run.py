import pandas as pd
import requests
from urllib.parse import urlparse

# Read the Excel file
df = pd.read_excel('sample.xlsx')

# Function to extract file ID from Google Drive link
def extract_file_id(drive_link):
    parsed_url = urlparse(drive_link)
    if parsed_url.netloc == 'drive.google.com' and parsed_url.path.startswith('/file/d/'):
        return parsed_url.path.split('/')[3]
    else:
        return None

# Iterate over each row
for index, row in df.iterrows():
    # Get the Google Drive link from the 8th column
    drive_link = row[7]  # Assuming column indexing starts from 0

    # Extract file ID from Google Drive link
    file_id = extract_file_id(drive_link)

    # Check if the file ID is extracted successfully
    if file_id:
        # Construct the download link for the PDF file
        download_link = f"https://drive.google.com/uc?id={file_id}"

        # Download the PDF file from the Google Drive link
        response = requests.get(download_link)

        # Check if the request was successful
        if response.status_code == 200:
            # Specify the path to save the PDF file
            filename = f"pdf_{index}.pdf"  # Save the file with .pdf extension

            # Save the PDF content to a file
            with open(filename, 'wb') as f:
                f.write(response.content)

            print(f"PDF downloaded successfully for row {index + 1}.")
        else:
            print(f"Failed to download PDF from {drive_link} for row {index + 1}")
    else:
        print(f"Invalid Google Drive link '{drive_link}' for row {index + 1}. Please check the URL format.")
