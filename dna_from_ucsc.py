import sys
import urllib

"""
Provide a BED file (chrom, start, end), and will query the UCSC database for each line and extract the sequence. 
"""

region_path = sys.argv[1]
url = "http://genome.ucsc.edu/cgi-bin/das/hg19/dna?segment=%s:%s,%s"

for line in open(region_path):
    sline = line.split()
    sequence = urllib.urlopen(url%(sline[0], sline[1], sline[2])).read().split("<DNA")[1].split(">")[1].split("<")[0].replace("\n", "")

    #reverse the sequence if the strand is reverse
    sequence = sequence.lower()
    if len(sline) > 5:
        if sline[5] == "-":
            new_seq = []
            for char in sequence[::-1]:
                if char == 'g':
                    new_seq.append('c')
                elif char == 'c':
                    new_seq.append('g')
                elif char == 'a':              
                    new_seq.append('t')      
                elif char == 't':              
                    new_seq.append('a')             
                else:
                    new_seq.append(char)

            sequence = ''.join(new_seq)


    print "%s\t%s"%(line.strip("\n"), sequence)



    
