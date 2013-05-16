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
    print "%s\t%s"%(line.strip("\n"), sequence)



    
