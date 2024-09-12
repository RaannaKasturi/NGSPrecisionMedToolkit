import subprocess
import os
import sys
import requests

def download(url, fname):
    # Download a file from a URL
    response = requests.get(url)
    with open(fname, 'wb') as f:
        f.write(response.content)
    return fname

def fastqc_check(fastq_file):
    #This function takes fastq file as input and returns the quality check of the file.
    '''
    # Check if the fastqc tool is installed
    fastqc_path = "./FastQC/fastqc"
    try:
        version = subprocess.run([fastqc_path, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(version.stdout)
    except FileNotFoundError:
        print("The fastqc tool is not installed.")
        sys.exit(1) 
    '''
    # Run the fastqc tool
    fastqc_html_file = subprocess.run(["./FastQC/fastqc", fastq_file], stdout=subprocess.PIPE)
    '''
    # Check if the fastqc html file exists
    fastqc_html_file = fastq_file.replace(".fastq", "_fastqc.html")
    if not os.path.exists(fastqc_html_file):
        print("The fastqc html file does not exist.")
        sys.exit(1)
        '''

    # Open the fastqc html file
    #subprocess.run(["open", fastqc_html_file])

def fastp_check(fastq_file):
    #This function takes fastq file as input and returns the quality check of the file.
    '''
    # Check if the fastq file exists
    if not os.path.exists(fastq_file):
        print("The fastq file does not exist.")
        sys.exit(1)

    # Check if the fastp tool is installed
    try:
        subprocess.run(["fastp", "--version"], stdout=subprocess.PIPE)
    except FileNotFoundError:
        print("The fastp tool is not installed.")
        sys.exit(1) #replace with install command
    '''

    # Run the fastp tool
    #fastp_html_file = fastq_file.replace(".fastq", "_fastp.html")
    front_trim = input("Enter the number of bases to be trimmed from the front: ")  
    if len(fastq_file) == 1:
        fastp_html_file = subprocess.run(["./fastp", "-i", fastq_file[0], 
                                          "-o", fastq_file[0].replace('.fastq', '', 1) + "_trimmed.fastq", 
                                          "--detect_adapter_for_pe", 
                                          "-f", front_trim, 
                                          "-g", 
                                          "-l", "50", 
                                          "-c", 
                                          "-h", "./Downloads/" + fastq_file[0] + "_fastp.html", 
                                          "-w", "10"],
                                         stdout=subprocess.PIPE)
        
    elif len(fastq_file) == 2:
        fastp_html_file = subprocess.run(["./fastp", "-i", fastq_file[0], 
                                          "-o", fastq_file[0].replace('.fastq', '', 1) + "_trimmed_1.fastq", 
                                          "-I", fastq_file[1], 
                                          "-O", fastq_file[1].replace('.fastq', '', 1) + "_trimmed_2.fastq", 
                                          "--detect_adapter_for_pe", 
                                          "-f", front_trim, 
                                          "-g", 
                                          "-l", "50", 
                                          "-c", 
                                          "-h", fastq_file[0].replace('_1.fastq', '', 1) + "_fastp.html", 
                                          "-w", "10"],
                                         stdout=subprocess.PIPE)
    else:
        print("Too many input files. Enter maximum of 2 files.")
        sys.exit(1)

    '''
    # Check if the fastp html file exists
    if not os.path.exists(fastp_html_file):
        print("The fastp html file does not exist.")
        sys.exit(1)

    # Open the fastp html file
    subprocess.run(["open", fastp_html_file])

    return None
    ''' 
def reference_genome_and_bwa():
    ref_gen_link = input("Enter the link to the reference genome: ")
    ref_genome_zipped = download(ref_gen_link, "./Downloads/reference_genome.fa.gz")
    ref_genome = subprocess.run(["gunzip", ref_genome_zipped], stdout=subprocess.PIPE)

    # indexing the reference genome using bwa
    subprocess.run(["./bwa/bwa", "index", "-a", "bwtsw", "-p", "reference_genome", "reference_genome.fasta"], stdout=subprocess.PIPE)

if __name__ == "__main__":
    print("QualityCheck")

    fastqc_input_files = input("Enter the fastq files for quality check by fastqc (if multiple files, separate them by comma): ")
    input_files = fastqc_input_files.strip().split(',')
    input_files = ["./test/" + fastq_file for fastq_file in input_files]

    for fastq_file in input_files: #ERR11468777_1.fastq
        fastqc_check(fastq_file)
    
    fastp_check(input_files)
    


