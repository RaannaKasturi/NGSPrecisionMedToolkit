from pysradb.sraweb import SRAweb
import re

db = SRAweb()
'''
srp_id = "SRP265425"
df = db.sra_metadata(srp_id, detailed = True) #Bioproject ID
print(df.loc[2][0]) # Extracts accession id (SRR ID) of the 3rd row
print(type(df.loc[2]))

srr_id = "SRR11085797"
df1 = db.sra_metadata(srr_id, detailed=True) #SRR ID = single run of a particular bioproject
print(df1)


# Convert SRX to SRR accessions
srx_accession = 'SRX4720625'
srr_accessions = db.srx_to_srr(srx_accession, detailed=True)
'''

# Download the SRR runs
#db.download("SRP265425", threads=4, out_dir='./pysradb_downloads')
#db.download("SRR11886735", threads=4, out_dir='./pysradb_downloads')

def download_sra_files(accession):
    # Download sra files using the specified SRP accession
    db.download(accession, out_dir="./pysradb_downloads")

def select_files_to_download(srp_id):
    flag = True
    srr_ids_list = []
    df = db.sra_metadata(srp_id, detailed = True)
    print(df)
    
    while flag:
        choice = input("Do you wish to download the entire project or specific runs ? (Enter 'all' or 'specific'): ")
        if choice == "all":
            download_sra_files(srp_id)
            flag = False

        elif choice == "specific":
            print("Select the files to download: ")
            selected_srr_ids = input("Enter the SRR IDs separated by space: ")
            flag = False
            for x in selected_srr_ids.split():
                srr_ids_list.append(x)
                download_sra_files(x)
        
        else:
            print("Invalid choice entered. Please enter 'all' or 'specific'.")
            flag = True


if __name__ == "__main__":
    #id = input("Enter the SRP /SRX / SRR / SRS / GSM / GSE ID: ")
    '''
    if re.match(r'SRP[0-9]+', id): # if entered BioProject ID
        select_files_to_download(id)
    else:
        print("Invalid ID entered. Please enter a valid SRP / SRX / SRR ID.")

    # Specify the SRP accession number
    '''
    #srp_accession = "SRP265425"  # Replace with desired SRP accession
    #download_sra_files(srp_accession)

    srp_accession = "SRP265425"  # Replace with desired SRP accession
    select_files_to_download(srp_accession)


