import requests
from datetime import datetime

def efetch(name, marker, webenv, key, rawdir):
    '''
    EFetch: Retrieve full records for each UID.
    Function calls NCBI's eutils EFetch to download information obtained from esearch.
    
    Base URL for EFetch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi
    ESearch documentation: https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.EFetch
    Parameters used:
        - db=nucleotide (required) -> set as nucleotide (same as ESearch).
        - WebEnv -> to fetch stored information from previous ESearch results.
        - query_key -> query key of previous ESearch results.
        - retmode = text -> results are displayed in text form.
        - rettype = fasta -> results are returned in FASTA format.
    '''
    # Set date for output file
    date = datetime.now().strftime("%Y%m%d")
    
    efetch = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&WebEnv=' + webenv + '&query_key=' + key + '&retmode=text&rettype=fasta')

    outfile = open(rawdir + marker + '_' + name + '_' + date + '_raw' + '.fasta', "w")
    outfile.write(str(efetch.content).replace('\\n', '\n').replace('\\n\\n', '\n\n').replace('b\"','').replace('\"', ''))
    outfile.close()
    
    print(marker + '_' + name + ' ' + 'file successfully created')
    
    return(marker + '_' + name + '_' + date + '_raw' + '.fasta') 