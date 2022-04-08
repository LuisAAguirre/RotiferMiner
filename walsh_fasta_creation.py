from datetime import datetime

def fasta_creation(file, outdir):
    # Set date for output file
    date = datetime.now().strftime("%Y%m%d")
    
    genes = {'ITS':[], '18S':[], '28S':[], 'COI':[]}

    fi = open(file, 'r')
    lines = fi.readlines()
    fi.close()

    for l in lines[1:]:
        sl = l.strip().split('\t')
        if sl[1] != 'sp.':
            genes[sl[6].upper()].append('>'+' '.join([sl[5], sl[0],sl[1]]) + '\n' + sl[-1] + '\n')
        else:
            genes[sl[6].upper()].append('>'+' '.join([sl[5], sl[0],sl[1],sl[2].split(',')[0].replace(' ','').replace('\"','')]) + '\n' + sl[-1] + '\n')
            
    for g in genes.keys():
        fo = open(outdir + g+'_'+'internal' + '_' + date + '.fasta','w')
        for l in genes[g]:
            fo.write(l)
        fo.close()