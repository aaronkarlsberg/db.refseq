import os
import subprocess


# input list of file paths to newly created fasta files. Each fasta contains 1 sequence which corresponds to the closest match
# to sequences for particular species in other databases. The filepaths link to fasta files containing these matched sequences. Now they must 
# be aligned before final concensus is generated.


# single_seq_fasta_filepaths contains [[contig1aspecies1, contig1bspecies1, contig1cspecies1],[contig2aspecies1, contig2bspecies1, contig2cspecies1]]
def generate_mauve(single_seq_fasta_filepaths, taxid)

files = ' '.join(single_seq_fasta_filepaths)
header = 

generate_mauve = "/Applications/Mauve.app/Contents/MacOS/progressiveMauve --output=/"+header+".xmfa "+ files
process = subprocess.Popen(makeblastdb.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
