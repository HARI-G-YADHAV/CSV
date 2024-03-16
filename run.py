import pandas as pd
import requests

# Read the Excel file
df = pd.read_excel('sample.xlsx')

# Iterate over each row
for index, row in df.iterrows():
    # Get the Google Drive link from the 8th column
    drive_link = row[7]  # Assuming column indexing starts from 0
    
    # Check if the URL is a string and starts with 'http://' or 'https://'
    if isinstance(drive_link, str) and drive_link.startswith(('http://', 'https://')):
        # Download the PDF file from the Google Drive link
        response = requests.get(drive_link)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Specify the path to save the PDF file
            filename = f"pdf_{index}.html"  # You may want to customize the filename
            
            # Save the PDF content to a file
            with open(filename, 'wb') as f:
                f.write(response.content)
                
            print(f"PDF downloaded successfully for row {index + 1}.")
        else:
            print(f"Failed to download PDF from {drive_link} for row {index + 1}")
    else:
        print(f"Invalid URL '{drive_link}' for row {index + 1}. Please check the URL format.")
