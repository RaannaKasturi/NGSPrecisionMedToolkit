import os
import subprocess
import requests
from tqdm import tqdm

def run_command_out(command, dir=None):
    print("Running command:", command)
    cmd = command.split()
    if dir:
        cmd[0] = dir+"/"+cmd[0]
    try:
        output = subprocess.check_output(cmd)
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the command:", e.output.decode())
        return cmd

def run_command(command, dir=None):
    print("Running command:", command)
    cmd = command.split()
    if dir:
        cmd[0] = dir + cmd[0]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError as e:
        return False
    
def download(url, fname, chunk_size=1024):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    if os.path.isfile(fname):
        print(f"File '{fname}' already exists.")
    else:
        try:
            resp = requests.get(url, headers=headers, stream=True)
            resp.raise_for_status()  # Raise an error for bad responses
            total = int(resp.headers.get('content-length', 0))
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
            print(f"Downloaded '{fname}' successfully.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
    return fname
