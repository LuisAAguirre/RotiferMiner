import sys

def count_clean(file, min, to_exclude, rawdir, cleandir, countdir):
   fasta_list = []
   boo = 0
   
   f = open(rawdir + file)
   lines = f.readlines()
   f.close()
   
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
   
   fasta_list.append([genus_species,genus,species,header,seq])
   
   print(len(fasta_list))
   
   #Write out cleaned fasta file
   genus_count = {}
   
   fo = open(cleandir + file.split('_raw')[0] + '_clean.fasta', 'w')
   seq_count = 0
   for fasta in fasta_list:
      if len(fasta[4]) > min and fasta[1] not in to_exclude[0]:
         seq_count +=1
         fo.write(fasta[3] + '\n' + fasta[4] + '\n')
         if fasta[0] in genus_count:
            genus_count[fasta[0]] += 1
         else:
            genus_count[fasta[0]] = 1
   
   fo.close()
   print(to_exclude[0])
   #Write out Genus count list in CSV form
   fo = open(countdir + file.split('_raw')[0]+'.txt','w')
   print('Number of different genera: %s\n'%len(genus_count.keys()))
   print('Number of sequences kept: %s'%seq_count)
   for g in genus_count.keys():
      fo.write(','.join(g.split('_')) + ',' + str(genus_count[g]) + '\n')
   fo.close()
