from Bio import SeqIO
filename = "NC_000913.faa"
for record in SeqIO.parse(filename, "fasta"):
	print(f"Record {record.id}, length {str(len(record.seq))}")

