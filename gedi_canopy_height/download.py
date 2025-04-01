import os
import requests
import posixpath
from tqdm.notebook import tqdm

def download(URL, filename):
    # Get the current file size if it exists
    existing_file_size = os.path.getsize(filename) if os.path.exists(filename) else 0
    # Request the file details using Range header if a partial file exists
    headers = {'Range': f'bytes={existing_file_size}-'} if existing_file_size else {}
    response = requests.get(URL, headers=headers, stream=True)

    # Check for resumable support (206 Partial Content response)
    if response.status_code not in (200, 206):
        raise Exception(f"Server does not support resuming or returned an error: {response.status_code}")

    # Determine total size based on Content-Range or Content-Length
    content_range = response.headers.get('Content-Range')
    if content_range:
        total_size = int(content_range.split('/')[-1])
    else:
        total_size = int(response.headers.get('content-length', 0)) + existing_file_size

    # Set mode to append if resuming, otherwise write
    mode = 'ab' if existing_file_size else 'wb'
    
    # Start download
    with open(filename, mode) as f, tqdm(
        initial=existing_file_size,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        desc=f"Downloading {posixpath.basename(URL)}"
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))

    print(f"Download completed: {filename}")