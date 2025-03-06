import sys
import matplotlib.pyplot as plt
import seaborn as sns
from Bio import SeqIO

filename = sys.argv[1]

seq_lengths = [len(record.seq) for record in SeqIO.parse(filename, "fasta")]

# plot histogram
sns.set_style("darkgrid")
plt.figure(figsize=(10,6))
sns.histplot(seq_lengths, bins=30, kde=True, color="skyblue")
plt.xlabel("Sequence Length", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.title("Distribution of Sequence Lengths", fontsize=16)

plt.show()