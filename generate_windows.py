"""
Generates windows given a bin, a step and a list of chromosome end coordinates 
"""
import sys
import argparse

parser = argparse.ArgumentParser(description='This script generates window files given a list of chromosomes and end positions. You can adjust size and step of the window.')
parser.add_argument('chrom_file', help='The chromosome length file. It requires only chromosome and end position')
parser.add_argument('--size', type=int, default=10000, help='Size of the windows. Default [%(default)s bases]')
parser.add_argument('--step', type=int, default=1000, help='Step of the windows. Default [%(default)s bases]')  
parser.add_argument('--path', default=None, help='Path for the output file. If not used, will print in stdout. Default[%(default)s bases]')  
args = parser.parse_args()

for line in open(args.chrom_file):
    chrom_name, chrom_end = line.split()
    for i, window_start in enumerate(range(1, int(chrom_end), args.step)):
        print "%s\t%s\t%s\twindow_%s\t0\t."%(chrom_name, window_start, window_start+args.size, i)

