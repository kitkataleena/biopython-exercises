import sys
from Bio import SeqIO

filename = sys.argv[1]
countLessThan100 = 0
count = 0
total = 0
for record in SeqIO.parse(filename, "fasta"):
	if len(record.seq) < 100:
		countLessThan100 += 1
		print(f"Record {record.id} is less than 100 basepairs long")
	total += len(record.seq)
	count += 1
print(f"{count} records, total length {total}")
	
