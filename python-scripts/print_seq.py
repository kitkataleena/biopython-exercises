import sys
from Bio import SeqIO
filename = sys.argv[1]
for record in SeqIO.parse(filename, "fasta"):
	print(f"{record.id} {record.seq[:10]}...{record.seq[-10:]}")

