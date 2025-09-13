import os
import requests
import numpy as np

def download_data(url, output_path):
    response = requests.get(url, stream=True)
    #check if response is ok
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        raise Exception(f"Failed to download file from {url}")