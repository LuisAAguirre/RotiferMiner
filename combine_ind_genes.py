import os

def combine_ind_genes(template, dirIn, fnameout):

   ft = open(template,'r')
   lines = ft.readlines()
   ft.close()

   genes = lines[0].strip().split('\t')[4:-1]
   print(genes)
   genera = {}

   for l in lines[1:]:
      sl = l.strip().split('\t')
      genera[sl[3]] = sl[0:4]

   species = {}
   genusgroups = {}
   files = os.listdir(dirIn)
   problems = []
   for f in files:
      if f[-4:] == '.txt':
         gIdx = genes.index(f.split('_')[0])
         fg = open(dirIn+'/'+f,'r')
         res = fg.readlines()
         fg.close()
         for l in res:
            sl = l.strip().split(',')
            if sl[0] in genera.keys():
               k = sl[0] + '_' + sl[1]
               if k in species.keys():
                  species[k][gIdx] = sl[2]
               else:
                  species[k] = ['0','0','0','0']
                  species[k][gIdx] = sl[2]
                  if sl[0] not in genusgroups.keys():
                     genusgroups[sl[0]] = []
                  genusgroups[sl[0]].append(k)
            else:
               problems.append([genes[gIdx],sl[0],sl[1],sl[2]])
         
   fo = open(fnameout+'.csv','w')
   fo.write(','.join(lines[0].split('\t')[0:4]) + ',Species,' + ','.join(genes) + '\n')
   #for l in lines[1:]:
   #   sl = l.strip().split('\t')
   #   fo.write(','.join(sl+genera[sl[1]]) + '\n')

   for g in genera.keys():
      if g in genusgroups.keys():
         for s in genusgroups[g]:
            fo.write(','.join(genera[g]) + ',')
            fo.write(s.split('_')[1] + ',')
            fo.write(','.join(species[s]) + '\n')
      else:
         fo.write(','.join(genera[g]) + ',,0,0,0,0\n')


   fo.close()

   fo = open(fnameout+'_oddballs.csv','w')
   fo.write('Gene,Taxa,Number Of\n')
   for p in problems:
      fo.write(','.join(p) +'\n')
   fo.close()
