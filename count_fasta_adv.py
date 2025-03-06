
import sys
from Bio import SeqIO
filename = sys.argv[1]   
count = 0
for record in SeqIO.parse(filename, "fasta"):
        count += 1
print(f"There were {str(count)} records in file {filename}")
