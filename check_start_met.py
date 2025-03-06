from Bio import SeqIO
filename = "PGSC_DM_v3.4_pep_representative.fasta"
bad = 0
for record in SeqIO.parse(filename, "fasta"):
	if not record.seq.startswith("M"):
		bad += 1
		print(f"{record.id} starts with {record.seq[0]}")
print(f"Found {str(bad)} records in {filename} which did not start with M")
