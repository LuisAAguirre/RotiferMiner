def count(file, countdir):
    file = open(file.name)
    lines = file.readlines()
    file.close()
    fasta_list = []
    boo = 0

    seq = ''
    for line in lines:
        if line[0] == '>':
            if boo != 0:
                fasta_list.append([genus_species,genus,species,header,seq])
            header = line.strip()
            sh = header.split()
            genus = sh[1]
            if sh[2] == 'sp.':
                species = sh[2] + ' ' + sh[3].replace('_', '-')
            else:
                species = sh[2]
            genus_species = genus + '_' + species
            seq = ''
            boo = 1
        else:
            seq = seq + line.strip()
    
    #fasta_list.append([genus_species,genus,species,header,seq])
            
    name = file.name.split('/')[-1]

    genus_count = {}
    seq_count = 0
    for fasta in fasta_list:
        seq_count = 0
        if fasta[0] in genus_count:
            genus_count[fasta[0]] += 1
        else:
            genus_count[fasta[0]] = 1

    fo = open(countdir + name.split('.')[0]+'.txt','w')
    #print('Number of different genera: %s\n'%len(genus_count.keys()))
    #print('Number of sequences kept: %s'%seq_count)
    for g in genus_count.keys():
        fo.write(','.join(g.split('_')) + ',' + str(genus_count[g]) + '\n')
    fo.close()