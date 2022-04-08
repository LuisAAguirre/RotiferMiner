import argparse
import os
import ncbi_esearch, walsh_fasta_creation

#########################################################################################################################
#                                             Rotifer Miner Arguments                                                   #
#########################################################################################################################
parser = argparse.ArgumentParser(description='Rotifer Miner: NCBI Nucleotide DB Genetic Marker Search.')

######                         General Arguments                           ######
general = parser.add_argument_group('General Options')

general.add_argument(
    '--outdir',
    required=True,
    help='Output directory path.'
)

######                         Arparse arguments for creating Gene Marker FASTA files from lab sequences                           ######
lab = parser.add_argument_group('Create FASTA files from internal lab sequences')

lab.add_argument(
    '--internal_file',
    help='Path to file from which genetic marker sequences will be extracted.'
)

######   Argparse arguments for finding and retrieving GenBank sequences   ######
miner = parser.add_argument_group('GenBank sequence mining options')

miner.add_argument(
    '-m',
    '--Monogononta',
    action='store_true',
    help= 'Searches for selected genetic markers for all organisms in the Monogononta subclass.'
)

miner.add_argument(
    '-b',
    '--Bdelloidea',
    action='store_true',
    help= 'Searches for selected genetic markers for all organisms in the in the Bdelloidea subclass.'
)

miner.add_argument(    
    '-r',
    '--Rotifera',
    action='store_true',
    help= 'Searches for selected genetic markers for all organisms in the in the Rotifera phylum.'
)

miner.add_argument(
    '--taxonomy_id',
    type=str,
    help= 'Custom search using NCBI Taxonomy ID. Used to search for desired genetic markers on entire taxonomic groups.'
)

miner.add_argument(
    '--taxon_rank',
    help='Custom search alternative to taxonomy ID. Use taxonomic rank of interest.'
    
)

miner.add_argument(
    '--ITS',
    action='store_true',
    help='Search for ITS genetic markers'
)

miner.add_argument(
    '--18S',
    action='store_true',
    dest='s18',
    help='Search for 18S genetic markers'
)

miner.add_argument(
    '--28S',
    dest='s28',
    action='store_true',
    help='Search for 28S genetic markers'
)

miner.add_argument(
    '--COI',
    action='store_true',
    help='Search for COI genetic markers'
)

######   Argparse arguments for cleaning and counting sequences retrieved from GenBank   ######

clean = parser.add_argument_group('Options to clean retrieved sequences')

clean.add_argument(
    '--min_length',
    type=int,
    help='Minimum sequence length. Sequences shorter than this value will be ignored.'
)

clean.add_argument(
    '--exclusion_list',
    nargs='+',
    action='append',
    help='List of terms found in FASTA headers that are wished to be excluded. Separate all terms by space.\
        Ex: --exclusion_list Uncultured UNVERIFIED:'
)

args = parser.parse_args()

#########################################################################################################################
#                                          Output directory creation                                                    #
#########################################################################################################################
if not os.path.exists(args.outdir):
    os.mkdir(args.outdir)
    
rawdir = args.outdir + '/raw_genbank_sequences/'
cleandir = args.outdir + '/clean_sequences/'
countdir = args.outdir + '/gene_count/'

if not os.path.exists(rawdir):
    os.mkdir(rawdir)
if not os.path.exists(cleandir):
    os.mkdir(cleandir)
if not os.path.exists(countdir):
    os.mkdir(countdir)

#########################################################################################################################
#                                                 Function calls                                                        #
#########################################################################################################################

def rotifer_miner(taxon):
    ncbi_esearch.esearch(taxon, rawdir, cleandir, countdir, args.min_length, args.exclusion_list, args.ITS, args.s18, args.s28, args.COI)

if args.internal_file:
    walsh_fasta_creation.fasta_creation(args.internal_file, cleandir)

if __name__ == "__main__":
    if args.Monogononta:
        rotifer_miner('10191')
        
    if args.Bdelloidea:
        rotifer_miner('44578')
        
    if args.Rotifera:
        rotifer_miner('10190')
        
    if args.taxon_rank:
        rotifer_miner(args.taxon_rank)
        
    if args.taxonomy_id:
        rotifer_miner('txid' + args.taxonomy_id)
