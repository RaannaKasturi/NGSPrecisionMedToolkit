'''
conversion of sra to fastq using fastq-dump
installations: fastqc
code to automatically analyze fastqc html files
installations: fastp - to trim the bad reads and analyze the files in html
'''

import os
import sys
import subprocess
import tarfile
import requests

def download(url, fname):
    # Download a file from a URL
    response = requests.get(url)
    with open(fname, 'wb') as f:
        f.write(response.content)
    return fname

def install_sra():
    print("SRA Toolkit not found. Please wait while we download it...")

    file = download(url="https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.1.1/sratoolkit.3.1.1-ubuntu64.tar.gz", fname="sratoolkit.tar.gz")
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

if __name__ == "__main__":
    print("Welcome to the Quality Check module!")