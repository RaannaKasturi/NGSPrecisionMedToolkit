import os
import tarfile
import requests
from tqdm import tqdm


def download(url: str, fname: str, chunk_size=1024):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    resp = requests.get(url, headers=headers, stream=True)
    total = int(resp.headers.get('content-length', 0,))
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=chunk_size):
            size = file.write(data)
            bar.update(size)
    return fname

def install_sra():
    print("SRA Toolkit not found. Please wait while we download it...")
    file = download(url="https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.1.1/sratoolkit.3.1.1-ubuntu64.tar.gz",
                    fname="sratoolkit.tar.gz")
    print("SRA Toolkit Downloaded")
    with tarfile.open(file, "r:gz") as f:
        f.extractall()
    print("SRA Toolkit Extracted")
    extracted_dir = "sratoolkit.3.1.1-ubuntu64"
    os.remove("sratoolkit.tar.gz")
    if os.path.exists(extracted_dir):
        os.rename(extracted_dir, "sratoolkit")
        print("SRA Toolkit Installed")
    else:
        print(f"Error: The directory '{extracted_dir}' does not exist after extraction.")

