# parse blast results and generate single seq fasta files

def adjusted_percent_identity(percent_identity, alignment_length, query_length, subject_length):
    max_length = max(max_length_db1, max_length_db2)
    adjusted_percent = (percent_identity*1.0 * alignment_length)/ max_length
    return adjusted_percent

# subject_length is what is stored in blastnDb query_length is the other sp fasta file.




def parse_blast_results():
	return