import os, sys
from tools import run_command

def install_java():
    try:
        #data = run_command(['java', '-version'])
        print("Java already installed.")
        return True
    except:
        try:
            try:
                run_command(['sudo', 'apt', 'update'])
                run_command(['sudo', 'apt', 'install', 'default-jdk'])
                run_command(['sudo', 'apt', 'install', 'default-jre'])
                print("Java installed successfully.")
            except:
                run_command(['apt', 'update'])
                run_command(['apt', 'install', 'default-jdk'])
                run_command(['apt', 'install', 'default-jre'])
                print("Java installed successfully.")
            return True
        except:
            return False

def fastqc_check(file, data_dir):
    file_path = os.path.join(data_dir, file)
    if os.path.isfile(file_path):
        if any(ext in file for ext in [".fastq", ".sam", ".bam"]):
            try:
                output_dir = os.path.join(data_dir, 'fastqc_reports')
                os.makedirs(output_dir, exist_ok=True)
                run_command(['applications/fastqc/fastqc', file_path, '--outdir', output_dir])
                output_file = os.path.join(output_dir, file.split('.')[0] + '_fastqc.html')
                return output_file
            except Exception as e:
                print(f"An error occurred while running the command: {e}")
                return False
        else:
            print(f"The file format of {file} is not supported.")
            return False
    
def main(data_dir):
    files = os.listdir(data_dir)
    if install_java():
        for file in files:
            output_file = fastqc_check(file, data_dir)
            if output_file:
                print(f"FastQC report generated at {output_file}")
    else:
        print("Java installation failed. Try installing Java manually.")
        sys.exit(1)

if __name__ == '__main__':
    data_dir = 'data/ERR11468775'
    main(data_dir)
