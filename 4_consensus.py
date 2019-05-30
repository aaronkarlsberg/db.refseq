from Bio import AlignIO
from Bio.Alphabet import IUPAC, Gapped
from Bio.Align import MultipleSeqAlignment
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Read xmfa mauve file into alignment. 
# Use .read() for One sequence from each fasta. Generate Consensus seq. 
# Generate Seq Record.  write to new file.


alignment = AlignIO.read("path/to/aligned_mauve_file.xmfa", "mauve")
print("Alignment length %i" % alignment.get_alignment_length())



for record in alignment:
    record.id[0:-11]


summary_align = AlignInfo.SummaryInfo(alignment)

gap_consensus = summary_align.gap_consensus(threshold = (2/3.0), ambiguous = "N", consensus_alpha =IUPAC.unambiguous_dna, require_multiple=0)

consensus_id = "id"
consensus_description = "description"


gap_consensus_seq_record = SeqRecord(gap_consensus, id=consensus_id, description=consensus_description)

# print(gap_consensus_seq_record.id)
print(gap_consensus_seq_record)

SeqIO.write([gap_consensus_seq_record], "gconsensus.fa", "fasta")
