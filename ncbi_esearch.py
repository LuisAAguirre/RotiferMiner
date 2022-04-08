import requests
import time
import ncbi_efectch, count_clean_sequences

def esearch(taxon, rawdir, cleandir, countdir, min_length, to_exclude, ITS = False, s18 = False, s28 = False, COI = False):
    '''
    ESearch: Search a text query in a single Entrez database.
    Function calls NCBI's eutils ESearch to search the Nucleotide database
    for the specified combination of organism(s) and specified barcoding genes (ITS, 18S, 28S, and COI)
    
    Base URL for searching NCBI: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi
    ESearch documentation: https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
    Parameters used:
        - db=nucleotide (required) -> searches nucleotide database in NCBI
        - term (required) -> terms to search for (in this case rotifer and gene of interest)
        - retmode=json -> to retrieve information in json format instead of the default format XML
        - usehistory=y -> Esearch UID results will be saved onto the History server and will be used directly
            in the subsequent efetch call. Also allows us to extract webenv and querykey variables for efetch.
        -retmax = 100000 -> EUtils default output is only 20 UIDs. 100,000 is the maximum number of UIDs allowed to be retrieved.
    '''
    
    name = ''
    if taxon == '10191':
        name = 'Monogonont'
    elif taxon == '44578':
        name = 'Bdelloid'
    elif taxon == '10190':
        name = 'Rotifera'
    else:
        taxon = taxon
    
    if ITS:
        esearch = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term=txid10191[Organism] AND internal transcribed spacer&retmode=json&usehistory=y&retmax=100000')
        esearch = esearch.json()

        # Extract WebEnv and query_key to use in EFetch
        file = ncbi_efectch.efetch(name, 'ITS', esearch['esearchresult']['webenv'], esearch['esearchresult']['querykey'], rawdir)
        
        count_clean_sequences.count_clean(file, min_length, to_exclude, rawdir, cleandir, countdir)       
        
        # Delay added to prevent calling API more times than allowed. Only 3 API calls allowed per second.
        time.sleep(.5)
    if s18:
        esearch = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term=txid10191[Organism] AND 18S&retmode=json&usehistory=y&retmax=100000')
        esearch = esearch.json()

        # Extract WebEnv and query_key to use in EFetch
        file = ncbi_efectch.efetch(name, '18S', esearch['esearchresult']['webenv'], esearch['esearchresult']['querykey'], rawdir)
        
        count_clean_sequences.count_clean(file, min_length, to_exclude, rawdir, cleandir, countdir)       
        
        # Delay added to prevent calling API more times than allowed. Only 3 API calls allowed per second.
        time.sleep(.5)
    if s28:
        esearch = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term=txid10191[Organism] AND 28S&retmode=json&usehistory=y&retmax=100000')
        esearch = esearch.json()

        # Extract WebEnv and query_key to use in EFetch
        file = ncbi_efectch.efetch(name, '28S', esearch['esearchresult']['webenv'], esearch['esearchresult']['querykey'], rawdir)
        
        count_clean_sequences.count_clean(file, min_length, to_exclude, rawdir, cleandir, countdir)       
        
        # Delay added to prevent calling API more times than allowed. Only 3 API calls allowed per second.
        time.sleep(.5)
    if COI:
        esearch = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term=txid10191[Organism] AND COI[Gene]&retmode=json&usehistory=y&retmax=100000')
        esearch = esearch.json()

        # Extract WebEnv and query_key to use in EFetch
        file = ncbi_efectch.efetch(name, 'COI', esearch['esearchresult']['webenv'], esearch['esearchresult']['querykey'], rawdir)
        
        count_clean_sequences.count_clean(file, min_length, to_exclude, rawdir, cleandir, countdir)       
        
        # Delay added to prevent calling API more times than allowed. Only 3 API calls allowed per second.
        time.sleep(.5)